import mysql.connector

class DatabaseUpdater:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="parkinglots"
        )
    mycursor = mydb.cursor()
    if mydb:
        print("success")


    def __init__(self,statuses,index):
        self.status = statuses
        self.index = index+1
    
    def update(self):
        sql = "INSERT INTO lot1 (id, status) VALUES (%s, %s)"
        val = (self.index, self.status)
        try:
            DatabaseUpdater.mycursor.execute(sql, val)
            DatabaseUpdater.mydb.commit()
        except:
            sql = "UPDATE lot1 SET status = '{}' WHERE id = '{}'".format(self.status,self.index)
            DatabaseUpdater.mycursor.execute(sql)
            DatabaseUpdater.mydb.commit()

    def delete(self):
        sql = "DELETE FROM lot1"
        DatabaseUpdater.mycursor.execute(sql)
        DatabaseUpdater.mydb.commit()




"""sql = "INSERT INTO lot1 (id, status) VALUES (%s, %s)"
val = (1, "True")
mycursor.execute(sql, val)



print(mycursor.rowcount, "record inserted.")"""