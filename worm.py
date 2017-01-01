from sys import argv

import os

script = argv
name=str(script[0])

cmd = 'start cmd.exe'
os.system(cmd)
os.mkdir('clone')
os.system(r"copy cmd.exe clone")
os.system(r"copy " + name +" clone")
