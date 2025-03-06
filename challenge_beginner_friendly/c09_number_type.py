try:
  number_input = input("Enter a number: ")
  number = float(number_input)

  if number > 0 : 
    print(f"POSITIVE")
  elif number < 0 : 
    print( f"NEGATIVE")
  else : 
    print("The number is zero.")
except ValueError:
  print("Please enter a valid number")