user_input1 = input("Enter student name: ")
user_input2 = input("enter student standard: ")
user_input3 = input("Enter marks of Maths: ")
user_input4 = input("Enter marks of Science: ")
user_input5 = input("Enter marks of S.S.: ")
user_input6 = input("Enter marks of English: ")
if (user_input1).isalpha():
     if (user_input2).isdigit():
       if ((float(user_input3)<18) or (float(user_input4)<18) or (float(user_input5)<18) or (float(user_input6)<18)):
         print(f"Sorry!!! You are fail...")
       else:
         percentage = (float(user_input3) + float(user_input4) + float(user_input5) + float(user_input6)) / 200 * 100
         print(f"----- Exam Report -----, Student name: {user_input1}, Student standard: {user_input2}, Percentage: {percentage}%" )
         #print(f"Student name: {user_input1}")
         #print(f"Student standard: {user_input2}")
         #print(f"Percentage: {percentage}%")
         print("pass")
         if percentage >= 70:
          print("Grade: Distinction")
         elif percentage >= 60:
          print("Grade: First Division")
         elif percentage >= 35:
          print("Grade: Second Division")
         else:
          print("Grade: Fail")
     else:
      print(f"{user_input2} should be valid standard")
else:
 print(f"{user_input1} is not valid Name")