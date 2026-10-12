playlist = ["Shape of you", "Blinding Lights", "Believer", "Perfect"]

print("len : ",len(playlist))

print("first : ", playlist[0])

print("last : ", playlist[-1])

playlist.append("Dynamite")

print("add Dynamite : ",playlist)

playlist.remove("Believer")

print("remove Dynamite : ",playlist)

playlist.sort()
print("sort : ",playlist)

for x, z in enumerate(playlist, start=1):
    print(x,z)
