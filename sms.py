import database
import datetime
import time
def all():
    ph = database.phone_number()
    print(ph)
    date = datetime.date.today()
    t = time.ctime()
    tax = database.taxamt()
    area = database.area()
    name = database.owner_name()
    from twilio.rest import Client
    account_sid = 'ACa0ddb2f69017fd1dbba510c0b9a02463'
    auth_token='d69f77b664f1d69067d2b2c83a17f32c'
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
                        
            body="Dear customer {} The amount of rupees {} has the debited from your account while crossing the toll booth at {} on {} {}".format(name,tax,area,date,t),
            from_='+15855348972', #should be verified
            to = '+916385553279'
            )
    print(message.sid)
all()