info = {
    "key": "Value",                       # string key-value pair
    "subject": ["Python", "Java", "Html"],# list as value
    "topics": ("dic", "sets"),            # tuple as value
    "name": "Biswas",                      # string as value
    "age": 32,                             # integer as value
    "Adult": True,                         # boolean as value
    "Marks": 43.2,                         # float as value
}

print(info)                 # print the entire dictionary
print(type(info))           # print the type → <class 'dict'>
print(info["name"])         # access value using key "name" → Biswas
print(info["age"])          # access value using key "age" → 32
