s = {"amir": 12, "reza": 16, "ali": 1, "mmd": 18, "javad": 13}

std = []

for n, s2 in s.items():
    if s2 >= 17:
        x = "perfect"
    elif s2 >= 14:
        x = "good"
    elif s2 >= 10:
        x = "pass"
    else:
        x = "reject"
    
    print(f"{n}: {s2} -> {x}")

    if s2 >= 10:
        std.append(n)

print("pass :", std)

total = sum(s.values())
z = len(s)
avg = total / z
print("avg : ", avg)

top = max(s, key=s.get)
print("top: ", top)
