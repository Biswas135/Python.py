# type conversion

a = "2"          # a is a string
b = int("2")     # converting string "2" into integer → 2
c = 4.25         # c is a float
d = str(a)       # converting a (string) again into string → still "2"

print(type(a))   # shows type of a → <class 'str'>
print(type(b))   # shows type of b → <class 'int'>
print(type(d))   # shows type of d → <class 'str'>
print(b + c)     # integer + float → float result → 2 + 4.25 = 6.25
