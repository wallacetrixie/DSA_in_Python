#pop removes its key but returns the value
person = {
    "name": "John",
    "age": 25
}

age = person.pop("age")

print(age)
print(person)