"todos os numeros da sequencia de fibonnaci começam com o 0, então já é adicionado logo de inicio"
listNumber = [0] 

def fibonnaci(qtdNumbersToCalculate, number = 1):
    listNumber.append(number)
    if listNumber.__len__() < qtdNumbersToCalculate:
        fibonnaci(qtdNumbersToCalculate, number + listNumber[-2])
    return listNumber

"A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square (Source: https://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers)"
def is_perfect_square(number):
    square = number ** 2
    return square * square == number

def is_number_fibonnaci(numberToFind):
    if numberToFind == 0:
        return True
    return is_perfect_square(5 * numberToFind * numberToFind + 4) or is_perfect_square(5 * numberToFind * numberToFind - 4)
        
for i in range(10):
    if is_number_fibonnaci(i) == True:
        print("{} is fibonnaci".format(i))
    else:
        print("{} not fibonnaci".format(i))