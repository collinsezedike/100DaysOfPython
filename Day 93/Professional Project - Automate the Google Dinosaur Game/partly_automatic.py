import pyautogui
import time

X_COR = 490
Y_COR = 210
COLOR = (172, 172, 172)

print("Engines started...open Chrome now!")
time.sleep(5)   # enough time to switch to your chrome tab
pyautogui.keyDown("up") # starts the game

while True:
    s = pyautogui.screenshot()
    if s.getpixel((X_COR, Y_COR)) == COLOR or s.getpixel((X_COR, Y_COR+10)) == COLOR or\
        s.getpixel((X_COR, Y_COR+20)) == COLOR or s.getpixel((X_COR, Y_COR+30)) == COLOR or \
        s.getpixel((X_COR+10, Y_COR)) == COLOR or s.getpixel((X_COR+10, Y_COR+10)) == COLOR or\
        s.getpixel((X_COR+10, Y_COR+20)) == COLOR or s.getpixel((X_COR+10, Y_COR+30)) == COLOR or \
        s.getpixel((X_COR+20, Y_COR)) == COLOR or s.getpixel((X_COR+20, Y_COR+10)) == COLOR or\
        s.getpixel((X_COR+20, Y_COR+20)) == COLOR or s.getpixel((X_COR+20, Y_COR+30)) == COLOR or \
        s.getpixel((X_COR+30, Y_COR)) == COLOR or s.getpixel((X_COR+30, Y_COR+10)) == COLOR or\
        s.getpixel((X_COR+30, Y_COR+20)) == COLOR or s.getpixel((X_COR+30, Y_COR+30)) == COLOR:
        pyautogui.keyDown("up")

    # to restart after failing
    if s.getpixel((650,190)) == COLOR:
        print("Starting a new game...")
        pyautogui.keyUp("up")
