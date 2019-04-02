import time
import string


print('\n---------------------Example 1---------------------\n')

time.sleep(1.75)
print("Griffin: Hey Malcom! Don't forget the birthday cake when you come today evening, okay?")
time.sleep(2)
print('\n')
print('Malcom is typing...\n')
time.sleep(2.5)
print('Malcom: Sure Griffin! No problem. I will be there at 5:30.')

print('\n')

time.sleep(2.5)
print("System: Hold on Malcom! You have an appointment at 05:30 PM with Dr. Jones. You will only be able to reach Griffin's at 6:30 PM.")
print('\n')
time.sleep(4)
print("I suggest you keep the doctor's appointment and postpone your arrival at the birthday party by 1 hour. Shall I update Griffin?\n")
value = raw_input()
print('\n')

#user input
if value == "Yes, please":
    print('Great! I have sent an updated message to Griffin. He is fine with this.')
    print('\n')
else:
    print("\nOkay. The doctor's appointment has been moved to tomorrow 05:30 PM.")
    print('\n')
	
time.sleep(4)

print('\n---------------------Example 2---------------------\n')

time.sleep(2)
print('Jessica: Hey Wendy, movie tonight? I hear La La Land is amazing.')
print('\n')
time.sleep(2)
print('Wendy is typing...\n')
#time.sleep(2.5)
#print("Wendy: Sure Jessica. Let's go!")
#print('\n')
time.sleep(2.5)
#print('Jessica: Great! See you at 08:45 tonight.')
print("System: Wait Wendy! You have a conference call at 9:00 PM. You should be free by 09:30 PM.")
time.sleep(3)
print("\nShould I book your movie for 10:00 PM?")
print('\n')

value = raw_input()

if value == "Yes, that sounds good.":
    print('Great! Your movie is booked at 10:00 PM, PVR Cinema, Acropolis Mall')
    time.sleep(2)
    print('I have updated Jessica.')
    time.sleep(2)
    print('The cab will pick you up at 09:40 PM. Enjoy your movie!')
    print('\n')
    time.sleep(3)
elif value == "Nope":
    time.sleep(2.5)
    print('\n')
    print("Then, should I book tickets for tomorrow morning show? You will be free by 10:00 AM and you can reach at your office by 11:30, On time...!!")
    value2 = raw_input("User:")
    if value2 == "Yes":
        time.sleep(3)
        print('La La Land is booked for tomorrow 8:00 AM at Cinepolis, Acropolis Mall. Have a great time!\n')
    else:
        time.sleep(1.7)
        print("Okay! No Problem Wendy, I'll book tickets for you two for this weekend, by that time you both will be free from your office work and  other stuffs. ")
else:
	print('\n')
	time.sleep(2)
	print("Okay! No Problem Wendy, I'll book tickets for you two for this weekend, by that time you both will be free from your office work and  other stuffs.")
	print('\n')
