import time
display=""
ram=""
ram3=[]
ram2=False
def textshow(text="null", wait=0.1, screen_lines=5):
    global display
    display=""
    for i in range(len(text)):
        display=display+text[i]
        print("\n" * 1000)
        print(display)
        print("\n" * screen_lines)
        time.sleep(wait)
def textadd(text="null", wait=0.1, screen_lines=5):
    global display
    for i in range(len(text)):
        display=display+text[i]
        print("\n" * 1000)
        print(display)
        print("\n" * screen_lines)
        time.sleep(wait)
def clearscreen():
    print("\n" * 1000)
def textremove(num1=1, num2=3):
    global ram
    global ram3
    global display
    ram=""
    ram3=[]
    for i in range(num1, num2):
        ram3.append(i)
    for i in range(len(display)):
        if i not in ram3: 
            ram=ram+display[i]
    display=ram
def update(screen_lines):
    print("\n" * 1000)
    print(display)
    print("\n" * screen_lines)

#showcase
textshow("imma type some funny text." , 0.01, 0)
time.sleep(1)
textshow("fart poop fart fart", 0.01, 0)
time.sleep(2)
textshow("kinda boaring imma delete this text", 0.01, 0)
time.sleep(2)
textshow("fart poop fart fart", 0.01, 0)
time.sleep(1)
for i in range(len(display)):
    textremove(len(display) - 1, len(display))
    update(0)
    time.sleep(0.1)
