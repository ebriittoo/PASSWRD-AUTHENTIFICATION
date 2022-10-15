import getpass

database = {"aman.kharwal": "123456", "kharwal.aman": "654321"}

username = input("Enter your username :")

password = getpass.getpass("Enter your password : ")

for i in database.keys():

    if username ==  i:
    
        while password != database.get(i):

            password = getpass.getpass("Enter your password Again : ")

            break

        print("Verified")