# -*- coding: utf-8 -*-
import traceback

from functools import wraps
from queue import Queue
from .utils import HelpOptions

class SelfbotHook:

    def __init__(self, client, settings={}, commands={}, queue: Queue = None):
        self.client = client
        self.settings = settings
        self.commands = commands
        if not queue: queue = Queue(0)
        self.queue = queue

    def gen_help(self, key='', options=HelpOptions):
        res_list = {}
        res = options.Prefix
        for head, commands in self.commands.items():
            no = 0
            for cmd, val in commands.items():
                no += 1
                if head is None:
                    res += '\n%s' % options.Left
                    if options.Num: res += options.Num % no
                    res += key
                    res += cmd.title() if val['title'] else cmd
                    if val['args']: res += ' ' + (options.ArgsLeft + options.ArgsSep.join(val['args']) + options.ArgsRight)
                    if options.Doc and val['func'].__doc__: res += options.DocSep + val['func'].__doc__
                    continue
                elif head not in res_list:
                    res_list[head] = ''
                res_list[head] += '\n%s' % options.Left
                if options.Num: res_list[head] += options.Num % no
                res_list[head] += key
                res_list[head] += cmd.title() if val['title'] else cmd
                if val['args']: res_list[head] += ' ' + (options.ArgsLeft + options.ArgsSep.join(val['args']) + options.ArgsRight)
                if options.Doc and val['func'].__doc__: res_list[head] += options.DocSep + val['func'].__doc__
        for head in res_list:
            res += '\n' + options.Header % head
            res += res_list[head]
        res += '\n' + options.Footer
        return res.strip()

    def worker_msg(self):
        functions = [cmd['func'] for cmd in [self.commands[head].values() for head in self.commands]]
        while True:
            msg = self.queue.get()
            if msg is None:
                return
            for func in functions:
                value = func(msg)
                if value == 'error':
                    break
                elif value:
                    break

    def put_msg(self, msg):
        self.queue.put(msg)

    def process(self, msg, users, groups, permissions):
        pcheck = execute = False
        if msg._from != self.client.profile.mid and not self.settings['public']:
            return False
        if msg.toType == 2:
            if groups not in [[None], []]:
                if 'ALL' in groups or msg.to in groups:
                    pcheck = True
                elif [group for group in groups if group in self.settings['groups']]:
                    pcheck = True
        elif msg.toType == 0:
            sender = msg._from if msg._from != self.client.profile.mid else msg.to
            if users not in [[None], []]:
                if 'ALL' in users or sender in users:
                    pcheck = True
                elif [user for user in users if users in self.settings['users']]:
                    pcheck = True
        if pcheck:
            if 'ALL' in permissions:
                execute = True
            elif [permission for permission in permissions if msg._from in self.permissions[permission]]:
                execute = True
        return execute

    def parse_cmd(self, text):
        msg = text.lower()
        if self.settings['setKey']['status']:
            if msg.startswith(settings['setKey']['key']):
                cmd = msg.replace(settings['setKey']['key'], '')
            else:
                cmd = 'Undefined command'
        else:
            cmd = msg
        return cmd

    def command(self, alt: tuple = (), title: bool = True, cmd_args: list = [], head: str = None, name: str = None, users: list = ['ALL'], groups: list = ['ALL'], permissions: list = ['ALL'], inpart: bool = False, prefix: bool = True, usecmd: bool = True, register: bool = True, defer=None):
        def __wrapper(func):
            if register:
                if head not in self.commands:
                    self.commands[head] = {}
                self.commands[head][name if name else func.__name__] = {
                    'func': func,
                    'title': False if name else title,
                    'args': cmd_args,
                    'alt': alt,
                    'users': users,
                    'groups': groups,
                    'permissions': permissions,
                    'inpart': inpart,
                    'prefix': prefix,
                    'usecmd': usecmd
                }
            @wraps(func)
            def __check(*args, **kwargs):
                msg, text, txt, cmd, msg_id, receiver, sender, to, setKey = args[0]
                value = checked = execute = False
                command = name if name else func.__name__
                if not msg.contentType:
                    msg_text = cmd if usecmd else txt
                    if inpart and (msg_text.startswith(command) or msg_text.startswith(alt)):
                        checked = True
                    if checked:
                        execute = self.process(msg, users, groups, permissions)
                    if execute:
                        try:
                            value = True
                            kwargs = {'msg': msg, 'text': text, 'txt': txt, 'cmd': cmd, 'msg_id': msg_id, 'sender': sender, 'to': to, 'setKey': setKey}
                            func(*args, **kwargs)
                        except Exception:
                            value = 'error'
                            traceback.print_exc()
                        finally:
                            if defer: defer()
                return value
            return __check
        return __wrapper