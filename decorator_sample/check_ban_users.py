password = {"ali": "123445", "mohsen": "12343246745", "sadegh": "1235463445", "abas": "12343245", }
block_users = {"ali"}


def ban(fun):
    def inner(*args, **kwargs):
        if args[0] in block_users:
            return "this user banned"
        return fun(*args)

    return inner


@ban
def change_password(username, new_password):
    password[username] = new_password
    return "success"


print(change_password("sadegh","3223131"))
print(password)
