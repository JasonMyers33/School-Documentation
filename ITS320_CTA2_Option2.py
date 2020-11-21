#------------------------------------------------------------------------
# Program Name: Car Database
# Program Author: Jason Myers
# Program Objective:Provide a way to enter to enter a car brand, model,
#                     year, starting odometer, ending odometer, and the MPG
#                     Stored in a dictionary print the dictionary out
#-----------------------------------------------------------------------
# Pseudocode:
#           Assign a unique value to each car.
#           Enter the cars make, model, starting odometer, ending odometer,
#           and the MPG.
#           Check that the odometer readings are numbers and the ending value
#           is higher that the start
#           Check that the year is a valid car year
#           Check that the MPG is a valid MPG
#           Display the dictionary
#------------------------------------------------------------------------
# Program Inputs: Car make, model, year, odometer, and MPG
# Program Outputs: Print the dictionary 
#------------------------------------------------------------------------

#set empty dictionary
car_data= {}

#Set a variable for looping data entry
z = 0
#Set variable  for a unique number to each car because none of the infomation being entered is unique
car_number = 0

#Data entry 
while z < 1:  
  #Assigning a unique number to each car because none of the information being entered is unique
  car_number = car_number + 1
  car_make=input('Enter the Make: ')
  car_model=input('Enter the Model: ')
  #Forcing the car year to be a year cars were made.
  while True:
    try:
      car_year=input('Enter the 4 digit year the car was made: ')
      if int(car_year) >=1885 and int(car_year) <=2050:
        car_year=int(car_year)
        break
      else:
       print('Your entry must be four digits and between 1885 and 2050.')
    except ValueError:
      print('Your entry must be four digits and between 1885 and 2050.')
  #Forcing odometer start to be a number.
  while True:
    try:
      odometer_start=input('Enter starting odometer: ')
      odometer_start=int(odometer_start)
      break
    except ValueError:
      print('Enter starting odometer as a number only')
  #Forcing odometer end to be a number and greater than the odometer start.
  while True:
    try:
      odometer_end=input('Enter the ending odometer: ')
      if int(odometer_end) >= int(odometer_start):
        odometer_end = int(odometer_end)
        break
      else:
       print('Your ending odometer must be higher than your starting odometer')
    except ValueError:
      print('Enter ending odometer as a number only')
 #Forcing MPG to be a number and less than 150.
  while True:
    try:
      mpg=input('Enter estimated Miles Per Gallon: ')
      if int(mpg) >=0 and int(mpg) <=150:
        mpg=int(mpg)
        break
      else:
       print('A number less than 150 must be entered.')
    except ValueError:
      print('A number less than 150 must be entered.')

  car_data[car_number]=(car_make, car_model, car_year, odometer_start, odometer_end, mpg)
  #car_data[car_number]=car_model
  #car_data[car_number]=car_year
  #car_data[car_number]=odometer_start
  #car_data[car_number]=odometer_end
  #car_data[car_number]=mpg

  question=input("Do you want to enter any more cars?")
  if question=='n' or question=='N' or question=='No' or question=='no':
    z = 1

for x in car_data.items():
  print('\nCar Position:', car_number, '\n  Car Make:', car_make, '\n  Car Model:', car_model, '\n  Car Year:', car_year, '\n  Starting Odometer:', odometer_start, '\n  Ending Odometer:', odometer_end, '\n  Miles Per Gallon:  ', mpg)
