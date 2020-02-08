import os


# vars
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="css/style.css" />
</head>
<body>

</body>
</html>"""

css = """/*Обнуление*/
*{padding: 0;margin: 0;border: 0;}
*,*:before,*:after{-moz-box-sizing: border-box;-webkit-box-sizing: border-box;box-sizing: border-box;}
:focus,:active{outline: none;}
a:focus,a:active{outline: none;}
nav,footer,header,aside{display: block;}
html,body{height:100%;width:100%;font-size:100%;line-height:1;font-size:14px;-ms-text-size-adjust:100%;-moz-text-size-adjust:100%;-webkit-text-size-adjust:100%;}
input,button,textarea{font-family:inherit;}
input::-ms-clear{display: none;}
button{cursor: pointer;}
button::-moz-focus-inner{padding:0;border:0;}
a,a:visited{text-decoration: none;}
a:hover{text-decoration: none;}
ul li{list-style: none;}
img{vertical-align: top;}
h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight: inherit;}
/*--------------------*/

"""

dirs = ["img", "css", "fonts", "js", "scss"]
files = ["css/style.css", "index.html", "scss/style.scss"]
sec_files = ["robots.txt"]
texts = [css, html , css]
# /vars

# dirs
for dir in dirs:
    try:
        os.makedirs(dir)
    except:
        pass
# /dirs

# files
for file, text in zip(files, texts):
    with open(file, "w", encoding="utf-8") as f:
        f.write(text)

for file in sec_files:
    with open(file, "w", encoding="utf-8") as f:
        pass
# /files
