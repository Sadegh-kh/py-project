def sonsur(words):
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "**" * len(word)


gen_sans = sonsur(["fuck", "bitch"])
next(gen_sans)
print(gen_sans.send("Sadegh"))
print(gen_sans.send("Abas"))
print(gen_sans.send("fuck"))
print(gen_sans.send("Hossain"))
print(gen_sans.send("bitch"))
