import datetime

def time_games():
    print datetime.datetime.now()
    print datetime.datetime.utcnow()
    print (datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1))
    print (datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds()
    print int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds())
    unixs = (datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds()
    print (unixs*1000)%1000
    print "frames",(unixs * 1000) % 1000 // 40

if __name__ == '__main__':
    sunrise = 1485762037
    sunset = 1485794875

    sunrise_dt = datetime.datetime.fromtimestamp(sunrise)
    sunset_dt = datetime.datetime.fromtimestamp(sunset)

    print sunrise_dt.strftime("%Y-%m-%d")

    timestring = "2014-12-30"

    print datetime.datetime.strptime(timestring,"%Y-%m-%d")
