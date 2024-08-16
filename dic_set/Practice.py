dic = {
    "cat"   : "a small animal",
    "table" : ["a piece of furniture","list of facts and figure"]
}

print(dic)

subjects = {
    "python","java","c++","java","python","javascript"
}
print(len(subjects))

subjects1 ={}
x = int(input("Bangla marks :"))
subjects1.update({"Bangla": x}) 
x = int(input("Physics marks :"))
subjects1.update({"Physics": x}) 
x = int(input("Chemistry marks :"))
subjects1.update({"Chemistry": x}) 
print((subjects1))