import pymysql.cursors

def getData(beverage,area):

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123123',
                                 db='test4545',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `SALES` WHERE" \
                  " Pid =(Select id From product where name ='{0}')" \
                  "and Sid =(Select id From store where name ='{1}') ".format(beverage,area)

            cursor.execute(sql)
            #result = cursor.fetchone()
            records = cursor.fetchone()
            print("am here")
            print("Total rows are:  ", len(records))
            #return records
            #  print("Printing each row")
            list = [records['Mon'],records['Tue'],records['Wed'],records['Thu'],
                    records['Fri'],records['Sat'],records['Sun']]
            #for row in records:
           # list = []
            #list.append(records['Mon'])
         #   list.append(records['Tue'])
        #    list.append(records['Wed'])
            return list
    finally:
        connection.close()

