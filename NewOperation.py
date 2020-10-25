usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "customer" and passwordInput == "1234":
    print("Login successful!")
    print("----- NON SHOP -----")
    print("1.MAMA         6 THB")
    print("2.SOFT DRINK  15 THB")
    print("3.SNACK       20 THB")
    print("--------------------")
    selected = input("Plese select number >> ")
    pieces = int(input("Plese select pices >> "))
    print("--------------------")
    if selected == "1":
        price = 6
        vat = 7
        result = price+(price*vat/100)
        total = result * pieces
        print("Total",total,"THB")
        print("----- THANK YOU-----")
    elif selected == "2":
        price = 15
        vat = 7
        result = price + (price * vat / 100)
        total = result * pieces
        print("Total", total, "THB")
        print("----- THANK YOU-----")
    elif selected == "3":
        price = 20
        vat = 7
        result = price + (price * vat / 100)
        total = result * pieces
        print("Total", total, "THB")
        print("----- THANK YOU -----")
    else:
        print("Error starting again plese")
else:
    print("Login unsuccessful!")