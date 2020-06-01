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
            #print("record >> ", records)

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

            cursor.execute(sql)
            records = cursor.fetchone()

            #print("record >> ", records)
            return records
    finally:
        connection.close()

#getData('Coffee','Malleshwaram')