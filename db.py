#import mysql.connector as mc
import mariadb as mc

import sys

try:
    mydb = mc.connect(
        host = "localhost",
        user = "root",
        password = "don",
        #password = "",
        port = 3306,
        database = "classWork"
    )
except mc.Error as e:
    print("Encountered some problem")
    sys.exit(1)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS student(ID INT AUTO_INCREMENT PRIMARY KEY,\
    firstName VARCHAR(100),\
    secondName VARCHAR(100),\
    sirName VARCHAR(100),\
    gender VARCHAR(100),\
    course_title VARCHAR(100),\
    course_code VARCHAR(100),\
    regNumber VARCHAR(100))"
    )