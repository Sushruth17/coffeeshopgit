import pymysql.cursors

def getData(beverage,area):
    print("get data for --->",beverage," ",area)
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with connection.cursor() as cursor:
            sql = "SELECT Mon,Tue,Wed,Thu,Fri,Sat,Sun FROM `SALES` WHERE" \
                  " Pid =(Select id From product where name ='{0}')" \
                  "and Sid =(Select id From store where name ='{1}') ".format(beverage,area)

            cursor.execute(sql)

            records = cursor.fetchone()
            print("record >> ", records)

            if records != None:
                listu= [records['Mon'],records['Tue'],records['Wed'],records['Thu'],records['Fri'],
                         records['Sat'],records['Sun']]
            else:
                listu = []

            return listu
    finally:
        connection.close()


def getLocationDetails(area):
    print("get loc details for --->", area)
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with connection.cursor() as cursor:
            sql = "SELECT City,LAT,LON,AVGFOOTFALL,MON,TUE,WED,THU,FRI," \
                  "SAT,SUN FROM `sourcedata` WHERE" \
                  " LOCATION = '{}'".format(area)
            # {'id': 1, 'City': 'Bangalore', 'LOCATION': 'Vjnagar', 'LAT': 12.9714, 'LON': 77.5436, 'AVGFOOTFALL': 166.0,
            #  'MON': 122, 'TUE': 148, 'WED': 135, 'THU': 166, 'FRI': 174, 'SAT': 220, 'SUN': 197}
            testSQL="SELECT * FROM `sourcedata` WHERE LOCATION =  'Vjnagar' "
            cursor.execute(sql)

            records = cursor.fetchone()
            print("record >> ", records)

            if records != None:
                lista = [records['City'],records['LAT'], records['LON'],records['AVGFOOTFALL'],
                         records['MON'],records['TUE'],records['WED'],records['THU'],
                         records['FRI'],records['SAT'],records['SUN']]
            else:
                lista = []

            return records
    finally:
        connection.close()

#getData('Coffee','Malleshwaram')