number_input = input("Enter a number: " )

try:
  number = int(number_input)
  if number % 2 == 0 :
    print("EVENT")
  else : 
    print("ODD")
except ValueError:
  print("Please enter a number")