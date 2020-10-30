import pymysql
db = pymysql.connect(db='bokaro', user='root', passwd='bokaro', host='localhost', port=3306)
cursor = db.cursor()

def insertStudentRecord(db,cursor) :
    rollno = raw_input("Enter rollno - ")
    name = raw_input("Enter name - ")
    classs = raw_input("Enter classs - ")
    sql = "INSERT INTO pystudent (rollno, name, class) VALUES (%s, %s, %s)"
    cursor.execute( sql, (rollno, name, classs))
    cursor.close()
    db.commit()
    print 'Inserted Successfully'

def updateStudentRecord(db,cursor) :
    rollno = raw_input("Enter rollno whose record you want to update - ")
    classs = raw_input("Enter new class name to update - ")
    sql = "UPDATE pystudent set class = %s WHERE rollno = %s"
    cursor.execute(sql, (rollno,classs))
    cursor.close()
    db.commit()
    print 'Updated Successfully'

def getStudentRecord() :                  
    sql = "SELECT * from pystudent"
    cursor = db.cursor()
    cursor.execute(sql)
    for record in cursor:
        s = "RollNo: {}, Name: {} Class:{} \n\n".format(record[0],record[1],record[2])
        print(s)

insertStudentRecord(db,cursor)
#updateStudentRecord(db,cursor)        
#getStudentRecord()
db.close()

