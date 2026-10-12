x = int(input("age : "))
z = str(input("day : "))

price = 0

if x<5:
    price= 0
elif x>5 and x<12:
    price=50000
elif x>60:
    price=60000
else:
    price=100000

if z == "TUE" :
    d = price * (20/100)
    price = price - d

print("age : ", x)
print("day : ", z)

if price == 0 :
    print("price : free")
else:
    print("price : ", price)

