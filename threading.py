from threading import Thread
import os

rocket = 0


    



def func1():
    global rocket
    print("Staring Dave")
    os.system("python main.py")


t1 = Thread(target=func1)

t1.start()

def func2():
    global rocket
    print("Starting API")
    os.system("python api/main.py")

t2 = Thread(target=func2)

t2.start()
t2.join()
t1.join()
