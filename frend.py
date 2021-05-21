alpha="bcghjklmpqrtvwxyz"
score=0
names=input("enter first name and give space and than enter second name:- ")
for character in  names:
    if character in 'aeiou':
        score+=10
    if character in'friends':
        score+=20
        if character in alpha:
            score+=alpha.find(character)
        else:
            score+=0
if score>100:
    print('your friendship score is  : ',score)
    print('congrates! you both are best friends')
else:
    print("your friendship score is : ", score)