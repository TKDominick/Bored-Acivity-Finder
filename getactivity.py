import requests
import time
import pprint

dict = {}
while True:
	activity_by= input("Get an Activity: [R]andom, by [T]ype, by number of [P]articipants, by Price [R]ange, by [A]cessibility: ")
	if activity_by == 'R':
		resp = requests.get('http://www.boredapi.com/api/activity/')
		dict = resp.json()
		break
		
	elif activity_by == 'T':
		resp = requests.get('http://www.boredapi.com/api/activity/')
		dict = resp.json()
		
		break
		
	elif activity_by ==  'P':
		resp = requests.get('http://www.boredapi.com/api/activity/')
		dict = resp.json()
		
		break
		
	elif activity_by == 'R':
		resp = requests.get('http://www.boredapi.com/api/activity/')
		dict = resp.json()
		
		break
		
	elif activity_by == 'A':
		acessibilitymax = input("Input an accessibility max between 0 and 1, with 0 being the lowest: ")
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








