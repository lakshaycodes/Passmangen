
import string
import random
import harperdb

again = True
while again:
    masteerpass = input("Please Enter the Master Password:  ")
    if masteerpass=="masterpassword":
        schema = "password_repo"
        table = "main"
        opt = input('Please Select an option\n 1. View an existing Password\n 2.Create a new Password \n 3. Print All IDs and Application Names\n')

        db = harperdb.HarperDB(
                url="https://proj-carqr.harperdbcloud.com",
                username="admin",
                password="admin")

        def printpass(dta):
            for data in dta:
                print("ID: ", data["readable_ID"])
                print("Username: ", data["Username"])
                print("Password: ", data["password"])
                print("Application: ", data["Application"])

        if opt == "1":

            opt2 = input("Get Password Using: \n 1. Application Name\n 2. Password ID\n")

            if opt2=='1':
                application = input('Write the Application Name \n')
                application = "'%s'" % application
                dta = db.sql(f"select * from {schema}.{table} where Application={application};")
                printpass(dta)

            elif opt2 == "2":
                readid = input("Give The Password ID \n")
                readid =  "'%s'" % readid
                dta = db.sql(f"select * from {schema}.{table} where readable_ID={readid};")
                printpass(dta)
            
            else:
                print("Please Select A valid Option")

        elif opt == "2":
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation
            try:
                s = []
                s.extend(list(s1))
                s.extend(list(s2))
                s.extend(list(s3))
                s.extend(list(s4))
                random.shuffle(s)
                f = open('count.txt', 'r')
                data = f.read()

                readid = int(data)

                f.close()
                f = open('count.txt', 'w')
                f.write(str(readid + 1))
                f.close()
                plen = int(input("Enter the length of the password:"))
                
                s = ("".join(s[0:plen]))
                print(s)
                
                userName = input("Please enter the user name: ")
                password = s
                application = input("Please enter the Application Name here: ")

                db.insert(schema, table, [{
                "readable_ID": readid,
                "Username": userName,
                "password": password,
                "Application": application,
        }])
            except Exception as e:
                    print("There was an error:", e)
        elif opt=="3":
                dta = db.sql(f"select * from {schema}.{table};")
                for data in dta:
                    print("ID: ", data["readable_ID"])
                    print("Username: ", data["Username"])
                    print("Application Name: ", data["Application"])
                    print("\n")
            
        else:
            print("Please Select A valid Option")
        again = False
    else:
        print("Wrong Password")
        again = True
