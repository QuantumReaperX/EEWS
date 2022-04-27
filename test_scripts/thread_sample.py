from threading import *
import time

class MyThread(Thread):
    def __init__(self):
        self.running = True
        Thread.__init__(self)

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            print('Doing something')
            time.sleep(1.0/60)


thread = MyThread()
thread.start()