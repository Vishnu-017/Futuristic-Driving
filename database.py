import mysql.connector
import location
import detect

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*****"  # Replace with your actual password
)

# Function definitions
def phone_number(ph):
    return ph[0] if ph else None

def taxamt(tax):
    return tax[0] if tax else None

def area(tollname):
    return tollname

def owner_name(name):
    return name[0] if name else None

def main():
    try:
        mycursor = mydb.cursor()
        
        # Get vehicle number from detect module
        vehicle_no = detect.vech_no()
        
        # Fetching user details
        query = "SELECT * FROM vechile.owner_details WHERE Vechicle_No = %s"
        mycursor.execute(query, (vehicle_no,))
        owner_details = mycursor.fetchone()
        if owner_details:
            print("Owner Details:", owner_details)
        else:
            raise Exception("No owner details found")

        # Fetching Pan card
        query = "SELECT Pan_card FROM vechile.owner_details WHERE Vechicle_No = %s"
        mycursor.execute(query, (vehicle_no,))
        pan = mycursor.fetchone()
        if not pan:
            raise Exception("No Pan card found")
        pan_card = pan[0]
        print("Pan Card:", pan_card)

        # Fetching bank details using JOIN
        query = """
            SELECT * FROM vechile.owner_details v
            JOIN bank.rbi r ON v.Pan_card = r.Pan_card
            WHERE r.Pan_card = %s
        """
        mycursor.execute(query, (pan_card,))
        bank_details = mycursor.fetchone()
        print("Bank Details:", bank_details)

        # Get toll information
        tollname = location.loc()
        print("Toll Name:", tollname)
        
        query = "SELECT taxes FROM toll.toll_names WHERE Names = %s"
        mycursor.execute(query, (tollname,))
        tax = mycursor.fetchone()
        if tax:
            tax_amount = taxamt(tax)
            print("Tax Amount:", tax_amount)
        else:
            raise Exception("No tax information found")

        # Fetch phone number
        query = "SELECT Phone_number FROM vechile.owner_details WHERE Vechicle_No = %s"
        mycursor.execute(query, (vehicle_no,))
        ph = mycursor.fetchone()
        if ph:
            phone = phone_number(ph)
            print("Phone Number:", phone)
        else:
            raise Exception("No phone number found")

        # Fetch owner name
        query = "SELECT User_name FROM vechile.owner_details WHERE Vechicle_No = %s"
        mycursor.execute(query, (vehicle_no,))
        name = mycursor.fetchone()
        if name:
            owner = owner_name(name)
            print("Owner Name:", owner)
        else:
            raise Exception("No owner name found")

        # Update bank savings
        query = "UPDATE bank.rbi SET Savings = Savings - %s WHERE Pan_card = %s"
        mycursor.execute(query, (tax_amount, pan_card))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

        # Verify update
        query = "SELECT * FROM bank.rbi"
        mycursor.execute(query)
        all_bank_records = mycursor.fetchall()
        print("Updated Bank Records:", all_bank_records)

    except Exception as e:
        print(f"Error: {str(e)}")
        mydb.rollback()
    
    finally:
        mycursor.close()
        mydb.close()

if __name__ == "__main__":
    main()
