username = "Aziz"
users = [
    {
        "name": "Aziz",
        "age": 20,
        "city": "Faisalabad"
    },
    {
        "name": "Ali",
        "age": 21,
        "city": "Lahore"
    }
]
 
results = [user for user in users if user["age"]>20]
print(results)