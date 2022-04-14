import time
from datetime import datetime as dt

hosts = 'hosts'
hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.hotmail.com']

while True:

    if dt(dt.now().year,dt.now().month,dt.now().day, 11) > dt.now() > dt(dt.now().year,dt.now().month,dt.now().day, 8):
        print('Working Hours....')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+'\n')


    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)                                    #seek method to place the pointer at the top  and then deleting all the lines below the pointer after the write command
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours....")
    time.sleep(5)
