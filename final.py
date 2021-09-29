import mysql.connector

my_db = mysql.connector.connect(host = '****',user = '***' , passwd = '*****8' , database = '***8')

print(my_db)

cursor = my_db.cursor()
cursor.execute('select NUMBER,message,date_format(TIME,"%H"),date_format(TIME,"%i") from whatsapp')
data = cursor.fetchall()
for x in data:
    print(x)

for x in data:
    import pywhatkit as kt
    import pyautogui as pg

    kt.sendwhatmsg(x[0],x[1],int(x[2]),int(x[3]),wait_time=30)
    pg.press('enter')
