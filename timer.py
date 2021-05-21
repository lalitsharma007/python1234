import threading
def lalit():
    print("lalit is great\n")
timer=threading.Timer(5.0,lalit)
timer.start()