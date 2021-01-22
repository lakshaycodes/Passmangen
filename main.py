import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    try:
        plen = int(input("Enter the length of the password:"))
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        s = ("".join(s[0:plen]))
        print(s)
        file = open("info.txt", 'a')
        userName = input("Please enter the user name: ")
        password = s
        website = input("Please enter the website address here: ")

        usrnm = "UserName: " + userName + "\n"
        pwd = "Password: " + password + "\n"
        web = "Website: " + website + "\n"

        file.write("---------------------------------\n")
        file.write(usrnm)
        file.write(pwd)
        file.write(web)
        file.write("---------------------------------\n")
        file.write("\n")
        file.close
    except Exception as e:
        print("There was an error:", e)