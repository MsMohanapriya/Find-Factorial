def FactorialRecursion(number):
    if number==1:
        return 1
    return FactorialRecursion(number-1)*number
number=int(input("enter the number : "))
print(FactorialRecursion(number))