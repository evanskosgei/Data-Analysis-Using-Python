import mariadb as mc
import sys

try:
    mydb = mc.connect(
        host = "localhost",
        user = "root",
        password = "don",
        port = 3306,
        database = "none"
    )
except mc.Error as e:
    print("Encountered some problem")
    sys.exit(1)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS REG (RID INT AUTO_INCREMENT PRIMARY KEY,\
    NAME varchar(255) NOT NULL,\
    CONTACT varchar(255),\
    EMAIL varchar(255),\
    GENDER varchar(255),\
    CITY varchar(255),\
    STATE varchar(255))"
);