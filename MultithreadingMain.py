from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello class prints num {} ".format(i))
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi class prints num {} ".format(i))
            sleep(1)


t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.1)
t2.start()

# We are asking the main thread to wait for the child threads to join with below code, but either of them
t1.join()
t2.join()


print("Bye")
