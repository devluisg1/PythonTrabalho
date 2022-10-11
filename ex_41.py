import sys
"""
arg1 = sys.argv[1]
arg2 = sys.argv[2]
"""

gasolina = float(input("Valor da Gasolina: "))
etanol = float(input("Valor do Etanol: "))

if gasolina * 0.7 < etanol:
    print("Compensa mais a Gasolina")
else:
    print("Compensa mais o Etanol")