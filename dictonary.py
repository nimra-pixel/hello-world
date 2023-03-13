dict1 = {
  "Student_name": "Angel",
  "Rollno": 234,
  "GPA":4.1,

}
print(dict1)
dict1["GPA"]=3.8
print(dict1)
dict1['passed']=True
print(dict1)
print(dict1["Rollno"])
print(dict1["GPA"])
print(dict1.keys())
print(dict1.values())
print(dict1.get('GPA'))
print(dict1.items())
dict1.update({'Rollno':230})
print(dict1)
dict1.update({"section":'A'})
print(dict1)
dict1.pop('Rollno')
print(dict1)
dict1.popitem()
print(dict1)
del dict1["GPA"]
print(dict1)
dict1.clear()
print(dict1)
dict1 = {
  "Student_name": "Angel",
  "Rollno": 234,
  "GPA":4.1,

}
for x in dict1:
  print(x) 
  print(dict1[x])

for x in dict1.keys():
  print(x)
  
for x in dict1.values():
  print(x)

for x,y in dict1.items():
  print(x,y)

dict2 = dict1.copy()
print(dict2)