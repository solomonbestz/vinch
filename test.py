numbers = [2, 4, 9, 1, 8, 3]

max_number = 0
for n in numbers:
    for m in numbers:
        if n > m:
            max_number = n
        else:
            n = m
        

print(max_number)

