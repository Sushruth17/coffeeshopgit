import pymysql.cursors

def getData(beverage,area):
    print("get data for --->",beverage," ",area)
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT Mon,Tue,Wed,Thu,Fri,Sat,Sun FROM `SALES` WHERE" \
                  " Pid =(Select id From product where name ='{0}')" \
                  "and Sid =(Select id From store where name ='{1}') ".format(beverage,area)

            cursor.execute(sql)
            #result = cursor.fetchone()
            records = cursor.fetchone()
            print("record >> ", records)
            #print("am here")
           # print("Total rows are:  ", len(records))
            #return records
            #  print("Printing each row")
           # print(type(records))
            #print(type(records['Mon']))
            #listu = []
            if records != None:
                listu= [records['Mon'],records['Tue'],records['Wed'],records['Thu'],records['Fri'],
                         records['Sat'],records['Sun']]
            else:
                listu = []
            #listuu = str(listu)
            #print(list)
            #for row in records:
            #listu = []
            #for rows in records:
         #       list.append(records[rows])
       #     print(listu)
         #   list.append(records['Tue'])
        #    list.append(records['Wed'])
            #print("record >> ", records)
            return listu
    finally:
        connection.close()

#getData('Coffee','Malleshwaram')