#Задача 2: Найдите сумму цифр трехзначного числа.

#*Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трехзначное число "))
number = int(number)
 
c = number % 10
number = number // 10
b = number % 10
number = number // 10
 
print("Сумма цифр числа:", number + b + c)