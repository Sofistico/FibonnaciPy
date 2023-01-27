"todos os numeros da sequencia de fibonnaci começam com o 0, então já é adicionado logo de inicio"
listNumber = [0] 

def fibonnaci(qtdNumbersToCalculate, number = 1):
    listNumber.append(number)
    if listNumber.__len__() < qtdNumbersToCalculate:
        print(number)
        fibonnaci(qtdNumbersToCalculate, number + listNumber[-2])
    print(listNumber)
        
fibonnaci(100)