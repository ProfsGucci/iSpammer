import time #You need to import this! if your using a Windows use command *pip install {pack}* witch in this case is time
import pyautogui # if your using windows use command *pip install {pack}*




print(" __ _______                                          ")
print("|__|   _   .-----.---.-.--------.--------.-----.----.")
print("|  |   1___|  _  |  _  |        |        |  -__|   _|")
print("|__|____   |   __|___._|__|__|__|__|__|__|_____|__|  ")
print("   |:  1   |__|                                      ")
print("   |::.. . |     Made By ProfsGucci                  ")
print("   `-------'                                         ")

add1 = input("Enter your spam lyrics here: ") # If you ever wanna add a text or a lyrics you can just write here. otherwise you can disable it with putting a # first!
add = open('spam.txt', 'r+')
add.write(add1)


wait = input("How much you want to wait: ") # How much you want to wait in seconds! it needs to ba a hole number!

if input("are you sure you wanna start the spamming? (y/n)") != "y": # Making sure that you wanna spam the user!
    exit()

time.sleep(int(wait))
print('Loading...')
time.sleep(1)
f = open("spam.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    time.sleep(5) # How fast the messages will be sent! ⚠️Youll need more ram for faster spamming. 8ram will be good  ⚠️
    pyautogui.press("enter")
print("        ")
print("        ")
print(f"Done Spamming!")

