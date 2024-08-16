#learning Dictonary
'''info = {
  "name"  : "Supriyo",
  "age"   : 21,
  "class" : 12,
  "subjects" : {
      "Physics" : "97",
      "Math"    : "95",
  }
}
print(info["name"])
info["surename"] = "Shaown"
info.update({"City" : "Bandarban",})
print(info)'''

#Learning Set #Don't Show the repeated values

lala = {1,2,3,4,5,6,6}
print(lala)  # I typed 6 twice but it only showed once

# creating a empty sets

lala1 = set()


#methord
'''Add values '''
lala1.add(7)
lala1.add(9)
print((lala1))

'''Remove'''
lala.remove(6)
print(lala)

'''Clear Sets'''
lala1.clear()
print(lala1)

'''Pop random items from sets'''

print(lala.pop())
print(lala.pop())

'''Union'''
set1 = {1,2,3}
set2 = {3,4,5}
Union = set1.union(set2)
print(Union)
"intersection"
inter = set1.intersection(set2)
print(inter)