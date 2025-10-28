password=input("Enter your password: ")
score=0
if len(password)>=8:
    score+=1
else:
    print("Your password should be atleast 8 characters")
if any(ch.islower() for ch in password) and any(ch.isupper() for ch in password):
    score+=1
else:
    print("Use both Uppercase And Lowercase Characters")
if any(ch.isdigit() for ch in password):
    score+=1
else:
    print("Use atleast one number")
special = "!@#$%^&*()-_=+[]{};:',.<>?/"
if any (ch in special for ch in password):
    score+=1
else:
    print("Use atleast one special characters")
if score==4:
    print("your password is strong")
elif score==3:
    print("Your password is guessable")
elif score==2:
    print("You need to be more harder")
else:
    print("try again")