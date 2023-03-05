import mysql.connector as c
from model_run import get_prediction

mydb=c.connect(host='localhost',user='root',passwd='usama78630mirzas',database='priceprediction')

# Adding to database
def addData(modId,year,meter,result):
    cursor=mydb.cursor()
    query='insert into Prediction values({},{},{},{})'.format(modId,year,meter,result)
    cursor.execute(query)
    mydb.commit()

# Deleting from database
def dropRow(modelID):
    query = f'delete from Prediction where userId = "{id}";'
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()

# Updating Database
def updateDatabase(modelId , yearMade , meterReading ,condition):
    price=get_prediction(modelid=modelId,YearMade=yearMade,meterReading=meterReading)
    query = f"update Prediction set ModelID='{modelId}',yearMade ='{yearMade}', meterReading ='{meterReading}', price='{price}' Where ModelID='{condition}';"
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()

