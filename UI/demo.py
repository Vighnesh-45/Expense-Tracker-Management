import mysql.connector as mc
import matplotlib.pyplot as plt
import numpy as np
print("Enter A Name: ")
name = input()
def data(nam):
    try:


        mydb = mc.connect(
            host="localhost",
            user="root",
            password="H@rSHiTR24",
            database="uni"
        )
        myc = mydb.cursor()
        qr = """select Student_id from Student where College_Name = %s"""
        myc.execute(qr, (nam,))
        rs = myc.fetchall()





        print(rs)

    except mc.Error as e:
        print("Error occured")


data(name)