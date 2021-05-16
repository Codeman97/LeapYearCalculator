# Determine whether entered year is or is not a leap year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
     print (str(year) + " is a leap year.")
    else:
      print(str(year) + " is not a leap year.")
  else:
    print(str(year) + " is a leap year.")
else:
  print(str(year) + " is not a leap year.")

  # Leap Years in 21st Century
  #  2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, and 2048
