import datetime
import winsound
sound = "alarm_sound.mp3"
repitions = 2
alarmHour=int(input("Enter your alarm hour: "))
alarmMinute=int(input("Enter your alarm minutes: "))
amPm=str(input("am or pm: "))

if (amPm=="pm"):
    alarmHour=alarmHour +12
while(1 == 1):
    if (alarmHour == datetime.datetime.now().hour and alarmMinute==datetime.datetime.now().minute):
        for i in range(repitions):
            winsound.PlaySound(sound, winsound.SND_ALIAS)
            
            
        def f(amPm,alarmHour):
            if (amPm=="am" and alarmHour>=4 and alarmHour<=8):
                print("\nGood morning.It's time to start your day's work.")
            elif (amPm=="am" and alarmHour>8 and alarmHour<=12): 
                print("\nHow are you planning your day?")
            elif(amPm=="pm" and alarmHour>12 and alarmHour<18):
                print("\nGood afternoon.")
            elif(amPm=="pm" and alarmHour >=18 and alarmHour<=21):  
                print("\nGood evening. Go and find something to eat foolish boy.")
            elif(amPm=="pm" and alarmHour>21 and alarmHour<=24):
                print("\nGood night, time for bed.")
            elif (amPm == "am" and alarmHour<=4):
                print("Get some more rest. it still dawn.")
        break 
print(f(amPm, alarmHour))  
print("\nYou've exited the loop.")
          
       
    