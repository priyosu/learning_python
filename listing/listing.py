'''marks = [87,65,45,45,23]
student = [87,"karan","Delhi"]
print(len(student[1]))'''


''' WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
mov1 = input("Enter the name of mov1 :")
mov2 = input("Enter the name of mov2 :")
mov3 = input("Enter the name of mov3 :")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)'''

#Practice 
'''WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)'''

test = [1,2,3,2,5]
new = test.copy()
new.reverse()
if(test==new):
    print("Palindrome")
else:
    print("Not")

