import datetime as dt
import random
import smtplib
now=dt.datetime.now()
today=now.weekday()

if today:
    with open('data.txt') as file:
        read_file=file.read()
        mylst=read_file.splitlines()
        quotes=random.choice(mylst)
    print(quotes)
    my_email='mahajanvedant765@gmail.com'
    my_password='gziotpimzcjpomqj'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='vedantmahajan004@gmail.com',msg=f'Subject:Daily Motivation\n\n{quotes}')