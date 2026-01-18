try:
  age=int(input("Enter your name:))
if age>=18:
  print("You are eligible to vote")
else:
  print("you are not eligible")
except ValueError:
  print("Please enter the valid interger for age")
