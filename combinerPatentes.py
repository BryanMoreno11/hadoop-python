#!/usr/bin/python3

import sys
subproblema = None
patentesCitantes = ''

for claveValor in sys.stdin:
    patenteCitada, patenteCitante = claveValor.strip().split("\t")
    # Primer subproblema
    if subproblema == None:
        subproblema = patenteCitada
    # Si corresponde al mismo subproblema
    if subproblema == patenteCitada:
        patentesCitantes += '{},'.format(patenteCitante)
    else:  # Si se acabó el subproblema, se emite
        print("%s\t%s" % (subproblema, patentesCitantes[0:-1]))
        # Pasar al siguiente subproblema
        subproblema = patenteCitada
        patentesCitantes = '{},'.format(patenteCitante)
# Si se acabó el último subproblema, se emite
print("%s\t%s" % (subproblema, patentesCitantes[0:-1]))
