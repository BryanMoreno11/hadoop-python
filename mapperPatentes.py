#!/usr/bin/python3

import sys
'''
Mapper de Patentes
Creado por Bertha Mazón y Maritza Pinta
'''
for linea in sys.stdin:
    patentea, patenteb = linea.strip() .split(",")
    if (patentea !='"CITING"'):
        print("%s\t%s" % (patenteb, patentea))