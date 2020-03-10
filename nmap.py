import os
import mysql.connector
import subprocess

red="200.33.171.20"

resultado = os.popen("nmap -sT "+red).readlines()
puertos= resultado[5:len(resultado)-2]



db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd="",
    database="nmap"
)

cursor= db.cursor()

for obj in puertos:
    fields = obj.split()
    sql = "INSERT INTO `puertos` (`nombre`, `status`, `service`) VALUES (%s, %s, %s)"
    val = (fields[0], fields[1], fields[2])
    cursor.execute(sql,val)

db.commit()
print (puertos)