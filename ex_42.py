from datetime import date

atual = date.today().year
ano = int(input("Digite o ano que você quer analisar: (Digite 0 para levar em conta o ano atual)"))

if ano == 0:
    ano = atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("Não é bissexto")



