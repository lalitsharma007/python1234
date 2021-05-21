# m1=input('input marks of student 1:')
# m2=input('input marks of student 2:')
# m3=input('input marks of student 3:')
# m4=input('input marks of student 4:')
# m5=input('input marks of student 5:')
# m6=input('input marks of student 6:')
# student_marks=[m1,m2,m3,m4,m5,m6]
# student_marks.sort()
# print(student_marks)
# a=input("enter your name\n")
# b=len(a)
# if b>10:
#     print("yes")
#
# else:
#     print("no")
# fruits=['apple','banana','plum','lalit']
# i=0
# num=int(input('enter number'))
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")
# n=4
# for i in range(4):
#     print("*" * (i+1))
# def greater(num1,num2,num3):
#     if(num1>num2):
#         if (num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3
# m=greater(23,5,677)
# print(f"the greatest no is{m}")
for i in range(1,21):
    with open(f"C:/Users/lalitsharma/Desktop/table/multiplication table of{i}.txt", 'w') as f:
     for j in range(1,11):
        f.write(f"{i}x{j}={i*j}")
        if j!=10:
            f.write('\n')
