from plyer import *
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\dsaya\\Downloads\\sail_boat_icon_183344.ico",
        timeout=10,
    )

if __name__ == '__main__':
    notifyMe("Hello","This is a simple desktop notification")
