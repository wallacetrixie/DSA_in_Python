#The clear methods wipes everything in the dictionary
Student={
    "name":"Wallace Wambulwa",
    "Age":22,
    "School":"co-operative university",
    "Location":"Nairobi"
}
Student.clear()
for key,value in Student.items():
    print(key,value)