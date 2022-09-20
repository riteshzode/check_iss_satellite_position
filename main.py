import requests
import datetime
import smtplib

MY_LAT = 19.8516
MY_LONG = 79.3499


def iss_check():
    iss = "http://api.open-notify.org/iss-now.json"

    r1 = requests.get(url=iss)
    iss_latitude = float(r1.json()["iss_position"]["latitude"])
    iss_longitude = float(r1.json()["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    sun_rise_set = "https://api.sunrise-sunset.org/json"

    para = {
        "lat": MY_LAT,
        "lng ": MY_LONG,
        "formatted": 0
    }

    r2 = requests.get(url=sun_rise_set, params=para)

    sun_rise = int(r2.json()["results"]["sunrise"].split('T')[1].split(":")[0])
    sun_set = int(r2.json()["results"]["sunset"].split('T')[1].split(":")[0])

    now_time = int(datetime.datetime.now().hour)

    if now_time <= sun_rise or now_time >= sun_set:
        return True


while iss_check() and is_night():
    my_email = 'chintupatil1666@yahoo.com'
    password = "zhywblthfizzxzmm"

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(from_addr=my_email,
                         to_addrs="mrperfectritesh143@gmail.com",
                         msg=f"Subject:Get up!\n\niss is up in the sky")
    print("Success")
