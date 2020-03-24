# LINE Python

*LINE Messaging's private API*

----

## Important
First things you have to do is, clone this repository [linepy-modified](https://github.com/crash-override404/linepy-modified)
and then you must to copy linepy folders, after all installation complete. Paste linepy folders to folder selfbot-py.  
Please do not sell or rent this source code, because this is just for learning.

## Installation for Termux

```sh
$ apt update
$ apt upgrade
$ apt install python
$ apt install git
$ git clone https://github.com/crash-override404/selfbot-py
$ cd selfbot-py
$ python -m pip install -r requirements.txt
$ python helloworld.py -a IOSIPAD
```

## Installation for VPS

```sh
$ git clone https://github.com/crash-override404/selfbot-py
$ cd selfbot-py
$ python3 -m pip install -r requirements.txt
$ python3 helloworld.py -a IOSIPAD
```

## Usage for V2
To register command you can use hook.command
```python
@hook.command
def something(*args, **kwargs):
    to = kwargs.get('to', None)
    line.sendMessage(to, 'Something command called')
```

You can use the optional for hook.command
* alt
⋅⋅⋅Alternative command for one function
⋅⋅⋅Type : tuple, Default : ()
* title
⋅⋅⋅Make command name title in help message (not used when name is set)
⋅⋅⋅Type : bool, Default : True
* cmd_args
⋅⋅⋅Additional arguments for using this function (use this with prefix)
⋅⋅⋅Type : list, Default : []
* head
⋅⋅⋅Set this function will stored where in help message (if None will stored at first section)
⋅⋅⋅Type : str, Default : None
* name
⋅⋅⋅Set name displayed in help message
⋅⋅⋅Type : str, Default : None
* users
⋅⋅⋅Set users permission to use this command
⋅⋅⋅Type : list, Default : ['ALL']
* groups
⋅⋅⋅Set groups permission to use this command
⋅⋅⋅Type : list, Default : ['ALL']
* permissions
⋅⋅⋅Set permissions to use this command
⋅⋅⋅Type : list, Default : ['ALL']
* inpart
⋅⋅⋅Set if you want call this command if anything in text contains command name or alt
⋅⋅⋅Type : bool, Default : False
* prefix
⋅⋅⋅Set if you want call this command if text prefix in command name or alt
⋅⋅⋅Type : bool, Default : False
* usecmd
⋅⋅⋅Set if you want call this command only if cmd used
⋅⋅⋅Type : bool, Default : True
* register
⋅⋅⋅Set if you want register this command to help message
⋅⋅⋅Type : bool, Default : True
* defer
⋅⋅⋅Set a lambda function to defer for execute after command executed
⋅⋅⋅Type : lambda, Default : None


## LINE Square
[HelloWorld Square](https://line.me/ti/g2/JGUODBE4RE)

## Discord
[HelloWorld](https://discord.gg/5jqbutB)

## Author
Zero Cool / [@crash-override404](https://github.com/crash-override404)  
Fadhiil Rachman / [@fadhiilrachman](https://www.instagram.com/fadhiilrachman)  
Alin / [@muhmursalind](https://github.com/muhmursalind)

## Support
All Hello World Members :  
Tanduri a.k.a HelloTan / [@hellotan](https://github.com/hellotan)  
Fauzan Ardhana / [@fauzanardh](https://github.com/fauzanardh)  
Moe Poi ~ / [@moepoi](https://github.com/moepoi)  
Muhammad Fahri / [@FAHRIZTX](https://github.com/FAHRIZTX)  
Dosugamea / [@Dosugamea](https://github.com/Dosugamea)  
Dzin / [@dzingans](https://github.com/dzingans)  
And others.
