grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
c = sum(grades[2]) / len(grades[2])
d = sum(grades[3]) / len(grades[3])
e = sum(grades[4]) / len(grades[4])
grades_sredniy = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]),
                  sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]),
                  sum(grades[4]) / len(grades[4])]
f = sorted(students)
g = {f[0]: grades_sredniy[0], f[1]: grades_sredniy[1], f[2]: grades_sredniy[2], f[3]: grades_sredniy[3],
     f[4]: grades_sredniy[4]}
print(g)

#Вариант 2. Так-то работает, но на выхоже не словарь, а список
index = 0
for average_rating in grades:
    grades[index] = sum(average_rating) / len(average_rating)
    index = index + 1

students_alfavit = sorted(students)

index = 0

slovar = students_alfavit

for name in students_alfavit:
    slovar[index] = {students_alfavit[index]: grades[index]}
    index = index + 1

print(slovar)




