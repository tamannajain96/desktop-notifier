#  Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

import datetime #for reading present date
import time
import requests #for retreiving coronavirus data from web
from plyer import notification  #for getting notification on your PC

#let there is no data initially
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    #if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")

# if we fetched data
if (covidData != None):
    # converting data into JSON format
    data = covidData.json()['Success']
    print(data)

    # repeating the loop for multiple times
    while (True):
        notification.notify(
            # title of the notification,
            title="COVID19 Stats on {}".format(datetime.date.today()),
            # the body of the notification
            message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                totalcases=data['cases'],
                todaycases=data['todayCases'],
                todaydeaths=data['todayDeaths'],
                active=data["active"]),
            # the notification stays for 50sec
            timeout=50
        )
        # sleep for 4 hrs => 60*60*4 sec
        # notification repeats after every 4hrs
        time.sleep(60 * 60 * 4)