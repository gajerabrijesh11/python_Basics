def calculator():
    while True:
        print("---simple calculator---")
        print("1. Add")
        print("2. Sub")
        print("3. Mul")
        print("4. div")
        print("5. Exit")

        choice = input("choose option (1-5)")
        if choice == "5":
            print("Cal close")
            break
        num1 = int(input("Enter No. 1 "))
        num2 = int(input("Enter No. 2 "))
        if choice == "1":
         print("Result:", num1 + num2)
        elif choice == "2":
         print("Result:", num1 - num2)
        elif choice == "3":
         print("Result:", num1 * num2)
        elif choice == "4":
         if num2 != 0:
          print("Result:", num1 / num2)
         else:
            print("Error div by zero")
        else:
          print("Invalid option")

calculator()