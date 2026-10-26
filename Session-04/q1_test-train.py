import math
import matplotlib.pyplot as plt

banana_lengths = [18, 20, 17, 22]
banana_widths = [3.5, 4.0, 3.2, 4.2]

apple_lengths = [8, 7.5, 8.5, 9]
apple_widths = [7.5, 8.0, 8.2, 8.5]

x_train = []

for i in range(len(banana_lengths)):
    x_train.append([banana_lengths[i], banana_widths[i], 0])

for i in range(len(apple_lengths)):
    x_train.append([apple_lengths[i], apple_widths[i], 1])

print("x_train : ",x_train)

for item in x_train:
    length = item[0]
    width = item[1]
    label = item[2]

    if label == 0:
        plt.scatter(length, width, color="orange", label="Banana")
    else: 
        plt.scatter(length, width, color="red", label="Apple")


new_fruit = [19, 3.8]
plt.scatter(
    new_fruit[0], new_fruit[1], color="green", marker="*", s=150, label="New Fruit"
)

plt.xlabel("Length")
plt.ylabel("Width")
plt.legend()
plt.show()

distances = []

for item in x_train:
    train_length = item[0]
    train_width = item[1]

    dist = math.sqrt(
        (new_fruit[0] - train_length) ** 2 + (new_fruit[1] - train_width) ** 2
    )
    distances.append(dist)


print()
print("distances : ",distances)
