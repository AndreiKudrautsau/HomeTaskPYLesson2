# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

n1 = None
n2 = None

s = int (input ("Введите подсказку №1 - сумму задуманных чисел №1 и №2> "))
p = int (input ("Введите подсказку №2 - произведение задуманных чисел №1 и №2> "))

for i in range (1, 1001):
    for j in range (1, 1001):
        if (i + j) == s and (i*j) == p:
            n1 = i
            n2 = j
print ("Задуманные числа> ", n1, "и", n2)
