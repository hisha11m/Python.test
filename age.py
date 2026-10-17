from  datetime import datetime
now = datetime.now()

print("Enter your date of birth in the required format DD-MM-YYYY ")

while True:
    user =  input()

    if user.strip().lower() == "exit":
     break

    try:
        birthday = user.split("-")

        day   =  (now.day   - int(birthday[0]))
        month =  (now.month - int(birthday[1]))
        age   =  (now.year  - int(birthday[2]))

        if now.month < int(birthday[1]) or (now.month == int(birthday[1]) and now.day < int(birthday[0])):
          age -= 1
        print(f"Your age is {age} years.")
        break

    except (ValueError, IndexError):
     print ("Please use the required format *DD-MM-YYYY* \nor write exit to leave")
