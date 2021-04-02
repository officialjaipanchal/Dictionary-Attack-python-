def readwordlist(path):
    try:
        wordlistfile = open("passwords.txt", "r").read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return wordlistfile


def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("\n Password Found In List :", guess_password)
            exit()


actual_password = input("Enter Password : ")
print("Your password Is :",actual_password,"\n")
actual_password_hash = hash(actual_password)

wordlist = readwordlist('passwords.txt')
guesspasswordlist = wordlist.split('\n')

# Running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)
# It would be executed if your password was not there in the wordlist
print(" \n it was not in Your Dictionary wordlist !!")

# Made By Jai Panchal.
