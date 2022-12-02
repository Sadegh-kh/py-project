start_char = lambda string, char: string[0] == char

text = "hello , how are you bro? , what's up?"
char = input("say your char : ")
print(start_char(text, char))
