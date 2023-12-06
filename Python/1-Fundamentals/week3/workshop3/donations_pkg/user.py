def login(database, username, password):
    for logkey, valuepassword in database.items():
        if username not in database:
            print("\nUser not found. Please Register")
            return ""
        if database[username] != password:
            print(f"\nIncorrect password for {username}!")
            return ""
        elif username in database and database[username] == password:
            print(f"\nWelcome back {username}!")
            return username


def register(database, username):
    if username in database.keys():
        print(f"\nUsername already registered.")
        return ""
    else:
        print(f"\nUsername '{username}' is registered!")
        return username
