words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "ai": "هوش مصنوعی",
    "java": "جاوا",
    "c": "سی",
    "c#": "سی شارپ",
    "c++": "سی پلاس پلاس"
}

x = "i love python and web and AI and java"

x_word = x.split()
result = []
true = 0
false = 0

for word in x_word:
    if word.lower() in words:
        result.append(words[word.lower()])
        true += 1
    else:
        result.append(f"[{word}]")
        false += 1

print(" ".join(result))
print("true:", true)
print("false:", false)
