import socket
import smtplib

from http.client import HTTPConnection
from email.mime.text import MIMEText

# Socket works
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.com", 80))
s.send(b'GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n')
get_request = s.recv(1024)
print(get_request)
s.close()


# HTTP works
conn = HTTPConnection('www.google.com')
conn.request('GET', '/')
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)
conn.close()

# SMTP ()
msg = MIMEText('This is a test email.')
msg['Subject'] = 'Test Email'
msg['From'] = 'max3koz@gmail.com'
msg['To'] = 'max3koz@gmail.com'

server = smtplib.SMTP('aspmx.l.google.com', 25)
server.starttls()
server.login('max3koz@gmail.com', '3KOZmax-6')
server.sendmail(msg['From'], msg['From'], msg.as_string())
server.quit()


def convert_date(date: str) -> str:
    # your code here
    date_list = date.split("/")
    print(date_list)
    date_reverse = date_list.reverse()
    print(date_reverse)
    if (len(date_list) > 3
        or ((int(date_reverse[1]) > 12 or int(date_reverse[1]) < 0))
        or ((int(date_reverse[0]) > 31 or int(date_reverse[0]) < 0))
    ):
        res = date_reverse[2] + "-" + date_reverse[1] + "-" + date_reverse[0]
    else:
        print("Error: Invalid date.")
    print(res)
    return res


print("Example:")
print(convert_date("01/01/2023"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")
'''

import re
import paramiko

def connect_and_fetch_cmd_log(name, pwd, ipaddr, cmd):
    result = ""
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    conn_try_limit = 10

    for i in range(conn_try_limit):
        try:
            print(f"connecting to divice... Attemt#{i+1} ")

            ssh_client.connect(ipaddr, username=name, password=pwd, look_for_keys=False)
            stdin, stdout, stderr = ssh_client.exec_command(cmd)
            result = stdout.readlines()
            break
        except Exception as error:
            print(f"An error has occured...{error}")
            print("/n")

    ssh_client.close()
    return result

connect_and_fetch_cmd_log("home3", "3KOZmax-6", "127.0.0.1", "pwd")