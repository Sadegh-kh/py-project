check_str = lambda string: str(string).replace(".", "").isdigit()

x = "23ad3"
for i in x.split():
    check = check_str(i)
    if not check:
        print("it isn't digital number")
        break
else:
    print("it's a digital number")
