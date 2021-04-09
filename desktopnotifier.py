from plyer import *
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=10,
    )

if __name__ == '__main__':
    notifyMe("Hello","This is a simple desktop notification")