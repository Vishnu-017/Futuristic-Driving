import database
import datetime
import time
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_toll_notification():
    """
    Send SMS notification about toll payment using Twilio
    
    Returns:
        bool: True if message sent successfully, False otherwise
    """
    try:
        # Get data from database
        phone = database.phone_number()
        if not phone:
            raise ValueError("No phone number retrieved from database")
            
        tax = database.taxamt()
        if not tax:
            raise ValueError("No tax amount retrieved from database")
            
        area = database.area()
        if not area:
            raise ValueError("No area retrieved from database")
            
        name = database.owner_name()
        if not name:
            raise ValueError("No owner name retrieved from database")
            
        # Get current date and time
        current_date = datetime.date.today()
        current_time = time.ctime()
        
        # Twilio credentials from environment variables
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        from_number = os.getenv('TWILIO_PHONE_NUMBER')
        to_number = phone  # Using the number from database
        
        if not all([account_sid, auth_token, from_number]):
            raise ValueError("Twilio credentials not properly configured")
            
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Create message body
        message_body = (
            f"Dear customer {name},\n"
            f"The amount of {tax} rupees has been debited from your account "
            f"while crossing the toll booth at {area} on {current_date} {current_time}"
        )
        
        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )
        
        print(f"Message sent successfully. SID: {message.sid}")
        print(f"Message sent to: {to_number}")
        return True
        
    except TwilioRestException as e:
        print(f"Twilio error: {str(e)}")
        return False
    except Exception as e:
        print(f"Error sending notification: {str(e)}")
        return False

if __name__ == "__main__":
    success = send_toll_notification()
    if success:
        print("Notification process completed successfully")
    else:
        print("Notification process failed")
