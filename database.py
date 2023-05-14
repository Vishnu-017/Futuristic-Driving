def phone_number():
  return ph[0]
def taxamt():
  return tax[0]
def area():
  return tollname
def owner_name():
  return name[0]
import mysql.connector
import location
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*****"
)
import detect
a=detect.vech_no()
mycursor = mydb.cursor()
#fetching user details
try:
  mycursor.execute("SELECT * FROM vechile.owner_details where Vechicle_No = '{}' ;".format(a))
  '''myresult = mycursor.fetchall()
  for x in myresult:
    print(x)
  '''
  myresult = mycursor.fetchone()

  print(myresult) 
  #selecting the pancard id to link the table
  mycursor.execute("SELECT Pan_card FROM vechile.owner_details where Vechicle_No = '{}' ;".format(a))
  pan = mycursor.fetchone()
  print(pan[0]) 

  #fetching bank details
  mycursor.execute("select * from vechile.owner_details as v, bank.rbi as r where v.Pan_card = r.Pan_card and r.Pan_card = '{}';".format(pan[0]))
  myresult = mycursor.fetchone()
  print(myresult)

  mycursor.execute("select * from bank.rbi as r where r.Pan_card = '{}';".format(pan[0]))
  myresult = mycursor.fetchone()
  print(myresult)


  tollname = location.loc()
  print(tollname)
  mycursor.execute("select taxes from toll.toll_names where Names = '{}';".format(tollname))
  tax = mycursor.fetchone()
  taxamt()
  print(tax[0])


  #fetching phone number 
  mycursor.execute("SELECT Phone_number FROM vechile.owner_details where Vechicle_No = '{}' ;".format(a))
  ph = mycursor.fetchone()
  phone_number()
  print(ph[0])


  #fetch name of the user
  mycursor.execute("SELECT User_name FROM vechile.owner_details where Vechicle_No = '{}' ;".format(a))
  name = mycursor.fetchone()
  owner_name()
  print(name[0])

  sql = "UPDATE bank.rbi as r set r.Savings = r.Savings-{} where r.Pan_card = '{}';".format(tax[0],pan[0])

  mycursor.execute(sql)

  mydb.commit()

  print(mycursor.rowcount, "record(s) affected")

  mycursor.execute("select * from bank.rbi as r;")
  myresult = mycursor.fetchall()
  print(myresult) 
  
except:
  print("Verification failed")
  

