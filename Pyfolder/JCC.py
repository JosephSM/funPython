# Joey's control center
import time
while True:    
    print("Ready to Study? (Yes or No)")
    study = input()
    if study == "Yes":
        print("How long would you like to set the pomodoro?")
        work_time = float(input())*60
        print("ready?")
        input()
        start_time = int(time.time())
        while(time.time() - start_time < work_time):
            time.sleep(.5)
            print((int(time.time())-start_time)%60)
            time.sleep(.5)
        print(int(time.time())-start_time)
        print("Break time!")






#I want this clock to work for me as a study tool
# Every time I run the program I want it to ask me how long to set the pomodoro

