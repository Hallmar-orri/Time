import time
class time():

    def __init__():
        self.start_time = 0
        self.pause_time = 0



    def start_stopwatch(self):
        pause = False
        self.start_time = time.time()

    

    def pause_stopwatch(self):
        pause = True
        curr_time = time.time() - self.start_time
        self.pause_time = curr_time + self.pause_time
    
    




    def stop_stopwatch(self):
        if pause == True:
            end_time = self.pause_time

        elif pause == False:
            curr_time = time.time() - self.start_time
            end_time = curr_time + self.pause_time
    





        
def convert_time(sec):
    min = sec // 60
    sec = sec % 60
    hour = min // 60
    min = min % 60
    print("time passed {0}:{1}:{2}".format(hour,min,sec))

    

