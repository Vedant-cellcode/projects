import requests
import datetime as dt
import smtplib
today=dt.datetime.now()
Hour=today.hour
my_lat=18.520430
my_lng=73.856743
my_email='mahajanvedant765@gmail.com'
my_password='Vedant@123'
other_email='vedantmahajan004@gmail.com'
contents='Look up in the sky and point out the ISS'
def iss_overhead():
    space_station = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_location = space_station.json()
    iss_location_lng = float(iss_location['iss_position']['longitude'])
    iss_location_lat = float(iss_location['iss_position']['latitude'])
    if my_lat-5<= iss_location_lat <=my_lat+5 and my_lng-5<= iss_location_lng <=my_lng+5:
        return True
def is_night():
    parameter = {'lat': my_lat, 'lng': my_lng, 'formatted': 0}
    website = requests.get(url='https://api.sunrisesunset.io/json', params=parameter)
    response = website.json()
    sunrise = int(response['results']['sunrise'].split(':')[0])
    sunset = int(response['results']['sunset'].split(':')[0]) + 12
    if Hour >sunset and Hour<sunrise:
        return True

if iss_overhead() and is_night():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"{other_email}", msg=f'Subject:Look up in the sky\n\n{contents}')


