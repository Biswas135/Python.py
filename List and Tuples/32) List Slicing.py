marks = [95, 32, 33, 42, 66, 43]      # list of marks

print(marks[1:])                      # from index 1 to the end → [32, 33, 42, 66, 43]

print(marks[:2])                      # from start to index 2 (not included) → [95, 32]

print([marks[1:3]])                   # slice index 1 to 3 (not included), then put inside another list → [[32, 33]]

print(marks[-3:-1])                   # negative indexing: elements at -3 and -2 → [42, 66]
