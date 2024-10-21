from datetime import date,datetime
from geopy.geocoders import Nominatim
import ephem
from geopy.geocoders import Nominatim
import requests
import calendar
from info import bs_years_data as check_dict , tithi_names , IMPORTANT_EVENTS

def conversion(year,month,day):
    engYear, engMonth, engDate=year,month,day
    #Define the least possible English date 1944/01/01 Saturday.
    startingEngYear=1944
    startingEngMonth=1
    startingEngDay=1
    dayOfWeek=calendar.SATURDAY
    #print(dayOfWeek)
    #Equivalent Nepali date

    startingNepYear=2000
    startingNepMonth=9
    startingNepday=17
    day_count=dayOfWeek

    #finding differences in the number of days between our starting date and provided eng date

    date_ref=date(startingEngYear,startingEngMonth,startingEngDay)
    date_provided=date(engYear,engMonth,engDate)
    diff=(date_provided-date_ref).days

    #initializing required nepali date i.e known refrence date
    nepali_Year=startingNepYear
    nepali_Month=startingNepMonth
    nepali_Day=startingNepday



    while diff!=0:
        #finding a number of days possible in that month of that year
        daysInMonth=check_dict[nepali_Year][nepali_Month-1]
        nepali_Day+=1

        if(nepali_Day>daysInMonth):
            nepali_Month+=1
            nepali_Day=1
        if(nepali_Month>12):
            nepali_Year+=1
            nepali_Month=1
        
        day_count+=1
        if(day_count>6):
            day_count=0
        diff-=1

   
    return nepali_Year,nepali_Month,nepali_Day,day_count




def get_current_location():
    # Get the device's current location based on IP address
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        location = data['loc'].split(',')
        latitude, longitude = location[0], location[1]
        return latitude, longitude
    except Exception as e:
        raise ValueError("Could not determine location: " + str(e))

def get_tithi(date_in):
    latitude, longitude = get_current_location()

    
    observer = ephem.Observer()
    observer.lat = latitude  
    observer.lon = longitude  
    
    date_in = ephem.Date(date_in)  
    observer.date = date_in

    # Get solar longitude
    sun = ephem.Sun(observer)
    solar_longitude = sun.hlon  

    # Get lunar longitude
    moon = ephem.Moon(observer)
    lunar_longitude = moon.hlon  

    
    new_moon = ephem.previous_new_moon(observer.date)

    
    lunar_age = observer.date - new_moon  

    
    tithi = int(lunar_age * 30 / 29.53) + 1  

    
    paksha = "Shukla Paksha" if tithi <= 15 else "Krishna Paksha"
    print(f'Tithi:{tithi_names[tithi]}, {paksha}')

    return tithi, paksha


def nepcalendar(year,month):
    day=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    months = ["Baishakh","Jestha","Ashadh","Shrawan","Bhadra","Ashwin","Kartik","Mangsir","Poush","Magh","Falgun","Chaitra"]
    monthMap={
        1:4,
        2:5,
        3:6,
        4:7,
        5:8,
        6:9,
        7:10,
        8:11,
        9:12,
        10:1,
        11:2,
        12:3
    }
    dayInmonth=check_dict[year][month-1]
    adMonth=monthMap[month]
    if adMonth==1 or adMonth==2 or adMonth==3:
        adYear=year-56
    else:
        adYear=year-57
    addate=27
    temp=conversion(adYear,adMonth,addate)
    day_count=temp[3]+1
    start_day=temp[2]
    while start_day!=1:
        day_count-=1
        if day_count<0:
            day_count=6
        start_day-=1
    print_calendar(dayInmonth,day_count)


def print_calendar(days_in_month, start_day):
    days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for day in days_of_week:
        print(f"{day} ", end="")
    print()
   
    for _ in range(start_day):
        print("    ", end="")  
    
    
    day = 1
    for _ in range(start_day, 7):
        print(f"{day:2}  ", end="")
        day += 1
    print()

    
    while day <= days_in_month:
        for _ in range(7):
            if day > days_in_month:
                break
            print(f"{day:2}  ", end="")
            day += 1
        print()


def AD_TO_BS(year,month,date):
    converted=conversion(year,month,date)
    lst=[converted[1],converted[2]]
    print(f'Year:{converted[0]}, Month:{converted[1]}, Date:{converted[2]}, {calendar.day_name[converted[3]]}')
    print()
    if(tuple(lst) in IMPORTANT_EVENTS):
        print(f'Important Event:{IMPORTANT_EVENTS[tuple(lst)]}')
    else:
        print('No Event')



def show_time():
    current_time=datetime.now()
    print(f'Time:{current_time}')