import requests

dict = {}
while True:
	while True:
		activity_by= input("Get an Activity: [R]andom, by [T]ype, by number of [P]articipants, by [Pr]ice Range, by [A]cessibility: ")
		if activity_by == 'R' or activity_by == 'r':
			resp = requests.get('http://www.boredapi.com/api/activity/')
			dict = resp.json()
			break
			
		elif activity_by == 'T' or activity_by == 't':
			acttype = input("Input activity type (education, recreational, social, diy, charity, cooking, relaxation, music, busywork): ")
			resp = requests.get('http://www.boredapi.com/api/activity?type='+acttype)
			dict = resp.json()
			
			break
			
		elif activity_by ==  'P' or activity_by == 'p':
			parts = input("Input number of participants: ")
			resp = requests.get('http://www.boredapi.com/api/activity?participants='+parts)
			dict = resp.json()
			
			break
			
		elif activity_by == 'Pr' or activity_by == 'pr':
			maxprice = input("Input a max price, with 0 being the lowest: ")
			resp = requests.get('http://www.boredapi.com/api/activity?minprice=0&maxprice='+maxprice)
			dict = resp.json()
			
			break
			
		elif activity_by == 'A' or activity_by == 'a':
			acessibilitymax = input("Input a max accessibility between 0 and 1, with 0 being the lowest: ")
			resp = requests.get('http://www.boredapi.com/api/activity?minaccessibility=0&maxaccessibility='+acessibilitymax)
			dict = resp.json()
			
			break
			
		else:
			print("Please enter a valid input: ")
			continue
	
	print("════════════════════════════════════════════════════════════════")
	print("")
	print(dict["activity"])
	print("Type: " + dict["type"])
	print("Participants: " + str(dict["participants"]))
	print("Price: " + str(dict["price"]))
	print("Accessibility: " + str(dict["accessibility"]))
	print("")
	print("════════════════════════════════════════════════════════════════")
	
	rerun = input("[R}erun or [Q]uit")
	if rerun == 'R' or rerun == 'r':
		continue
	elif rerun == 'Q' or rerun == 'q':
		break
	else:
		break









