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
        lis = patentesCitantes[0:-1].split(',')
        lis.sort()
        p = ",".join(str(element) for element in lis)
        print("%s\t%s" % (subproblema, p))
        
        # Pasar al siguiente subproblema
        subproblema = patenteCitada
        patentesCitantes = '{},'.format(patenteCitante)

# Si se acabó el último subproblema, se emite
lis = patentesCitantes[0:-1].split(',')
lis.sort()
p = ",".join(str(element) for element in lis)
print("%s\t%s" % (subproblema, p))
