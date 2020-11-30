def function():
 a = int(input('Введите число: '))
 b = int(input('Введите число: '))
 while a != 0 and b != 0:
        a = a * b
        b = int(input('Введите число: '))

 return a
 
a = function()
print(a)