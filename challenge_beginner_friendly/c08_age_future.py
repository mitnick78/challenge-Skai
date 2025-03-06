try:
  age_input = input("Enter your age: ")
  age = int(age_input) + 10

  if age <= 80 : 
    print( "In 10 years, you will be {age} years old")
  elif 81 <= age <= 100 : 
    print( f"In 10 years, you will be {age} years old great!!")
  else : 
    print("I think there's a problem lol")
except ValueError:
  print("Please enter a valid number")