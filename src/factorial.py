def factorial(number):
    aux = 1;
    for i in range(1, number+1):
        aux *= i
    return aux
