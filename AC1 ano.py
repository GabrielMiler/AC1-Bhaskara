ano = float(input("Informe ano"))

print(ano % 4 == 0 and ano % 100 != 0 or  ano % 400 == 0)
