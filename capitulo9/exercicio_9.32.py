#!/usr/bin/env python3

import os.path
import sys

procurar = sys.argv[1]
if len(sys.argv) < 1:
    print('Utilize de maneira correta o programa')
if len(sys.argv) == 2:
    if os.path.exists(procurar) and os.path.isdir(procurar):
        print('Existe e é um diretório')
    elif os.path.exists(procurar) and os.path.isfile(procurar):
        print('Existe e é um arquivo')
    else:
        print('Arquvio nao encontrado')