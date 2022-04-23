import datetime
import winsound

sound="alarm_sound.wav"
repetition=4
alarmHour=int(input("Alarm hour :  "))
alarmMinute= int(input("Alarm minute :  "))
amPm= str(input("Am or Pm :  "))

if amPm=="Pm":
    alarmHour=alarmHour+12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMinute==datetime.datetime.now().minute:
        for i in range(repetition):
            winsound.PlaySound(sound, winsound.SND_ALIAS)

        def time(amPm, alarmHour):
            if (amPm=="am" and alarmHour>=4 and alarmHour<=8):
                print("\nGood morning.It's time to start your day's work.")
            elif (amPm=="am" and alarmHour>8 and alarmHour<=12): 
                print("\nHow are you planning your day?")
            elif(amPm=="pm" and alarmHour>=12 and alarmHour<18):
                print("\nGood afternoon.")
            elif(amPm=="pm" and alarmHour >=18 and alarmHour<=21):  
                print("\nGood evening. Go and find something to eat foolish boy.")
            elif(amPm=="pm" and alarmHour>21 and alarmHour<=24):
                print("\nGood night, time for bed.")
            elif (amPm == "am" and alarmHour<=4):
                print("Get some more rest. it still dawn.")
    break   
print(time(amPm,alarmHour))
print("OUT of LOOP. ")