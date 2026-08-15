Student={
    "name":"Wallace Wambulwa",
    "Age":22,
    "School":"co-operative university",
    "Location":"Nairobi"
}
# adding new key
Student["course"]="Information Technology"
#updating existing key
Student["Age"]=23
print(Student["name"])
print(Student["Age"])
print(Student["School"])
print(Student["Location"])
print(Student.get("course"))
print(Student.get("studentID","Key not found"))