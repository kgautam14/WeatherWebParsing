import flask as flask
import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib, ssl

def main():

    page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
    status = page.status_code

    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast")

    # print(seven_day)

    period_tags = seven_day.select(".tombstone-container .period-name")
    periods = [pt.get_text() for pt in period_tags]

    short_desc_tags = seven_day.select(".tombstone-container .short-desc")
    short_desc = [st.get_text() for st in short_desc_tags]

    temp_tags = seven_day.select(".tombstone-container .temp")
    temp = [tt.get_text() for tt in temp_tags]

    weather = pd.DataFrame({

        "Period": periods,
        "Short_Desc": short_desc,
        "Temp": temp
    })

    # print(temp[0])
    # message = "Today's temperature would be %s "%(temp[0])
    # print(message)
    print(weather)


if __name__ == "__main__":
    main()