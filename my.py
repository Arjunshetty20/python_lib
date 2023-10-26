import mysql.connector
from datetime import date

config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': 3306,
    'database': 'learning'
}

def InsertUpdateDelete(sql):
    try:
        conn = mysql.connector.connect(**config)
        print("Connection successful")
        try:
            mycur = conn.cursor()
            mycur.execute(sql)
            conn.commit()
            mycur.close()
            return True
        except:
            conn.rollback()
            print("Syntax error")
            return False
        conn.close()
    except:
        print("Unable to connect to the database")

def DisplayTable(sql):
    try:
        conn = mysql.connector.connect(**config)
        print("Connection successful")
        try:
            mycur = conn.cursor()
            mycur.execute(sql)
            rows = mycur.fetchall()
            for row in rows:
                print(row)
            mycur.close()
        except:
            conn.rollback()
            print("Syntax error")
        conn.close()
    except:
        print("Unable to connect to the database")

while True:
    print("\nMain Menu")
    print("1. Book")
    print("2. User")
    print("3. Loan")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--BOOK--")
        print("1. Insert")
        print("2. Update")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice1 = input("Enter choice: ")
        if choice1 == "1":
            name = input("Enter book name: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            quantity = int(input("Enter book quantity: "))
            sql = f"INSERT INTO book(name, author, price, quantity) VALUES ('{name}', '{author}', {price}, {quantity})"
            result = InsertUpdateDelete(sql)
            if result:
                print("Book added")
        elif choice1 == "2":
            bookid = int(input("Enter book ID to update: "))
            name = input("Enter book name: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            quantity = int(input("Enter book quantity: "))
            sql = f"UPDATE book SET name = '{name}', author = '{author}', price = {price}, quantity = {quantity} WHERE bookid = {bookid}"
            result = InsertUpdateDelete(sql)
            if result:
                print("Book updated")
        elif choice1 == "3":
            bookid = int(input("Enter book ID to delete: "))
            sql = f"DELETE FROM book WHERE bookid = {bookid}"
            result = InsertUpdateDelete(sql)
            if result:
                print("Book deleted")
        elif choice1 == "4":
            sql = "SELECT * FROM book"
            DisplayTable(sql)
        elif choice1 == "5":
            break
        else:
            print("Enter a valid choice")
    elif choice == "2":
        print("\n--USER--")
        print("1. Insert")
        print("2. Update")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice2 = input("Enter choice: ")
        if choice2 == "1":
            name = input("Enter user name: ")
            address = input("Enter address: ")
            identitynumber = input("Enter ID number: ")
            mobile = input("Enter mobile number: ")
            email = input("Enter email: ")
            sql = f"INSERT INTO user(name, address, identitynumber, mobile, email) VALUES ('{name}', '{address}', '{identitynumber}', '{mobile}', '{email}')"
            result = InsertUpdateDelete(sql)
            if result:
                print("User added")
        elif choice2 == "2":
            userid = int(input("Enter user ID to update: "))
            name = input("Enter user name: ")
            address = input("Enter address: ")
            identitynumber = input("Enter ID number: ")
            mobile = input("Enter mobile number: ")
            email = input("Enter email: ")
            sql = f"UPDATE user SET name = '{name}', address = '{address}', identitynumber = '{identitynumber}', mobile = '{mobile}', email = '{email}' WHERE userid = {userid}"
            result = InsertUpdateDelete(sql)
            if result:
                print("User updated")
        elif choice2 == "3":
            userid = int(input("Enter user ID to delete: "))
            sql = f"DELETE FROM user WHERE userid = {userid}"
            result = InsertUpdateDelete(sql)
            if result:
                print("User deleted")
        elif choice2 == "4":
            sql = "SELECT * FROM user"
            DisplayTable(sql)
        elif choice2 == "5":
            break
        else:
            print("Enter a valid choice")
    elif choice == "3":
        print("\n--LOAN--")
        print("1. Insert")
        print("2. Update")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice3 = input("Enter choice: ")
        if choice3 == "1":
            bookid = int(input("Enter book ID: "))
            userid = int(input("Enter user ID: "))
            today = date.today()
            sql = f"INSERT INTO loan(bookid, userid, issuedate) VALUES ({bookid}, {userid}, '{today}')"
            result = InsertUpdateDelete(sql)
            if result:
                print("Loan added")
        elif choice3 == "2":
            loanid = int(input("Enter loan ID to update: "))
            bookid = int(input("Enter book ID: "))
            userid = int(input("Enter user ID: "))
            sql = f"UPDATE loan SET bookid = {bookid}, userid = {userid} WHERE loanid = {loanid}"
            result = InsertUpdateDelete(sql)
            if result:
                print("Loan updated")
        elif choice3 == "3":
            loanid = int(input("Enter loan ID to delete: "))
            sql = f"DELETE FROM loan WHERE loanid = {loanid}"
            result = InsertUpdateDelete(sql)
            if result:
                print("Loan deleted")
        elif choice3 == "4":
            sql = "SELECT * FROM loan"
            DisplayTable(sql)