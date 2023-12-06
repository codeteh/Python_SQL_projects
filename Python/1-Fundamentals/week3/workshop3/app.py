from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin": "password123"}
donations = []
authorized_user = ""

show_homepage()
if authorized_user == "":
    if True:
        print("You must be logged in to donate.")
    if False:
        print(f"Logged in as: {authorized_user}")


while True:
    option = input("Choose an option: ")
    if option == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = login(database, username, password)
        continue
    elif option == "2":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
        continue
    elif option == "3":
        if authorized_user == "":
            print(f"\nYou are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
        continue
    elif option == "4":
        show_donations(donations)
        continue
    elif option == "5":
        print(f"Leaving DonateMe...")
        quit()
    else:
        print("Invalid Choice: Please Try Again")
        continue
