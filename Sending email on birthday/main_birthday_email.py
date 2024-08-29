import pandas
import datetime as dt
import random
import smtplib
now=dt.datetime.now()
today=(now.month,now.day)
print(today)
data=pandas.read_csv('birthday.csv')
my_dict={(row.month,row.day):row for (index,row) in data.iterrows()}
if today in my_dict:
    with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as file:
        contents=file.read()
        Final_contents=contents.replace('[NAME]',my_dict[today]['name'].title())
    my_email='mahajanvedant765@gmail.com'
    my_password='jvul mlqu rdzc ozyw '
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{my_dict[today]['email']}", msg=f'Subject:Birthday wish\n\n{Final_contents}')
