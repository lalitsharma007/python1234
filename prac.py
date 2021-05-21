import  numpy as np
import pandas as pd

#
# n1=np.array([[10,20,30,45],[34,65,78,89]])
# print(n1)
# n2=np.zeros((3,5))
# print(n2)
# n3=np.full((3,3),10)
# print(n3)
# n4=np.arange(1,100,5)
# print(n4)
# n5=np.random.randint(1,50,10)
# print(n5)
# n6=np.array([[12,3,4,5,],
#              [9,87,67,32]])
# print(n6)
# print(n6.shape)
# n6.shape=(4,2)
# print(n6)
# a=np.array([16,45,67])
# b=np.array([15,90,89])
# print(np.column_stack([a,b]))
# s1=pd.Series([10,20,30,40,50])
# print(s1)
# d={"a":20,'b':30,'c':60}
# s2=pd.Series(d)
# print(
# student={"student name":['lalit','deva','pgl'],"students marks":[1,2,3]}
# print(pd.DataFrame(student))
# lalit=pd.read_csv("\\Users\\lalitsharma\\Desktop\\export.csv")
# print(lalit.head(10))
# print(lalit.iloc[0:5,0:4]
n1=np.array([10,20,30])
# print(n1)
n2=np.array([[10,20,30,40,50],[1,2,3,5,6,7,7]])
# print(n2)
n3=np.random.randint(100,300,5)
# print(n3)
s1=pd.Series([10,20,30,40,50,60])
# print(s1)
# students={"students_name":['lalit','sharma',"msdhoni"],'students_marks':[50,39,54,]}
# d=pd.DataFrame(students)
# print(d)
# export=pd.read_csv("\\Users\\lalitsharma\\Desktop\\export.csv")
# e=export.head(10)
# print(e)
# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)
