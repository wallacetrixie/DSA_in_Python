Student={
    "name":"Wallace Wambulwa",
    "Age":22,
    "School":"co-operative university",
    "Location":"Nairobi"
}
del Student["name"]

print(Student.get("name","Key not found"))