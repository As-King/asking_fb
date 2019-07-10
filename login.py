import os,sys,requests,json
import hashlib ,getpass
## Warna ##
m="\033[1;31m"
ht="\e[32;1m;5m"
gk="\033[5;32m"
gt="\033[1;32m"
g="\033[0;32m"
w="\033[1;37m"
c="\033[1;36m"
y="\033[1;33m"

#os.system('clear')
print ''
print '%s  LOGIN AKUN FACEBOOK '%(y)
id = raw_input('%s  Username :%s '%(gt,c))
pwd = getpass.getpass('%s  Password : '%(gt))
sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
x = hashlib.new('md5')
x.update(sig)
a = x.hexdigest()
data.update({'sig': a})
url = 'https://api.facebook.com/restserver.php'
r = requests.get(url, params=data)
z = json.loads(r.text)
print('%s  Login Succes'%(c))
token = open('token', 'w')
token.write(z['access_token'])
token.close()