word = (input("Enter what you want to say : "))
empt = []
for w in word.split():
    if len(w) >= 3:
        newords = "HDD" + w[1:] + w[0] + "ssd"
        empt.append(newords)
    else:
        empt.append(w)
encoder = " ".join(empt)
with open("quiz5.txt", "w") as f:
    f.write(encoder)
with open("quiz5.txt", "r") as f:
    text = f.read()
    print(text)
