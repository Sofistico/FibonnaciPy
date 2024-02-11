list = []
estadosAceitaveis = ['SP', 'RJ', 'MG', 'ES', 'Outros']
valores = [67836.43, 36678.66, 29229.88,27165.48, 19849.53]
totalSum = sum(valores)
for i in range(len(valores)):
    val = valores[i]
    estado = estadosAceitaveis[i]
    percent = (val / totalSum) * 100
    list.append((estado, val, percent))

print (list)