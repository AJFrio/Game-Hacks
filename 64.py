import pyautogui
import random
import time
# Get the screen size
screen_width, screen_height = pyautogui.size()

# Generate random coordinates within the screen size
start_x = random.randint(0, screen_width)
start_y = random.randint(0, screen_height)
end_x = random.randint(0, screen_width)
end_y = random.randint(0, screen_height)


while True:
    end_x = random.randint(0, screen_width)
    end_y = random.randint(0, screen_height)
# Move the mouse to the starting position
    pyautogui.moveTo(screen_width/2, screen_height/2)

# Hold and drag the mouse to the ending position
    pyautogui.dragTo(end_x, end_y, duration=2)
    time.sleep(.2)