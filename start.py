from controller import app
import controller
import setting
import threading


def initialize():
    setting.init()
    controller.monitor()


p = threading.Thread(target=initialize)
p.start()
print("hello there")
app.run()