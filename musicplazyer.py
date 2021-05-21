from pygame import mixer
mixer.init() #start the mixer
list=["happy.mp3",'song.mp3']

mixer.music.load("happy.mp3")
mixer.music.set_volume(0.9)
mixer.music.play()

while True:
    print("press 'p' to pause 'r' to resume ")
    print("press 'e' to exit the mixer")
    print("press 'f' to forward")
    query= input(">>> ")

    if query=='p' :
        mixer.music.pause()
    elif query=='r':
        mixer.music.unpause()
    elif query=='e':
        mixer.music.stop()
    elif query=='f':
        mixer.music.fadeout(2)
    break