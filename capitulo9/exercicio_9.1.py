#!/usr/bin/env python3
import sys
a = sys.argv[1] # pegando o primeiro argumento, o argumento 0 é o arq.py
with open(a, 'r') as arquivo:
    for x in arquivo:
        print(x)