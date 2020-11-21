import mysql.connector
from mysql.connector import errorcode
import json

# Open database connection with error handeling (I did not do any other error handeling).
try:
    connection = mysql.connector.Connect(
        host="localhost",
        user="jump",
        password="secret",
        database="world_x"
        )
    print('Connected to World X Database')
except mysql.connector.Error as problem:
  if problem.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Your username or password is incorrect")
  elif problem.errno == errorcode.ER_BAD_DB_ERROR:
    print('No such Database exists')
  else:
    print('You messed up something: ' + problem)
else:
  connection.close()

# Create a text file to export the display results for the assigment.
TextExport = open("Export_Population.txt","w")

# Start cursor object.
cursor = connection.cursor()

# Start SQL query and get the City ID, Name, current population, and future population.
Query = ("SELECT ID, Name, Info '$.Population', Population FROM city")
cursor.execute(Query)

# Fetch the data.
rows = cursor.fetchall()

# Some on screen notification that everything is progressing.
print('Starting caculation and exporting to text file.')

# Iterate JSON and make updates to population over a looping condition.
for row in rows:
    # Get the name of the city tied to is row number. This is used use for displaying the city later.
    CityName = row[1]
    # Get the value of info columntied to is row number.
    info = row[2]
    # Get the  population information from the JSON and assign to varable.
    pop = json.loads(info)
    # Assign the variable.
    CurrentPopulation = pop['Population']
    # Multiply the current population by 10%.
    TenPrecentPopulation = (pop['Population'] * 1.1)
    # Print the city name, current population, and the new population.
    TextExport.write('The city of '+CityName+' has a current population of {0:.0f}'.format(CurrentPopulation)+
                     '.\nAfter the 10% increase, the new population is {0:.0f}.\n\n'.format(TenPrecentPopulation))
    # Enter the new population number into the Population column.
    UpdateQuery = 'UPDATE city SET Population = %f where ID = %f'
    cursor.execute(UpdateQuery %(TenPrecentPopulation, row[0]))

# Commit the work to the database
connection.commit()

# Close the export file
TextExport.close()

# Close the SQL connection
connection.close()

# On screen notification the task is complete.
print('The task is complete.')
