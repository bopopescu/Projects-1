#!/usr/bin/eenv  python3
#encoding=utf-8
#lau.liu@9street.org
import  os
import sys
print(__file__)

print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(__file__))
DASE_DIR=(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(DASE_DIR)
from conf import  settings
from  core  import main
main.logginl()
settings.les()