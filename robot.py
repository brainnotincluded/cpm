from barcode import bar_code
from navigator import Navigator
from bellman.path_finder import find_path
from bellman.path_finder import visualize_plan
from utils import Brick
from bellman.config import Config
from RPLCD.i2c import CharLCD
import time


def lcd_blink():
    for i in range(6):
        lcd.backlight_enabled = False
        time.sleep(0.5)
        lcd.backlight_enabled = True
        time.sleep(0.5)
def lcd_print(msg):
    lcd.clear()
    lcd.cursor_pos = (2, 0)
    lcd.write_string(msg)
    
try:
    lcd = CharLCD('PCF8574', 0x27)
    b = Brick()
    n = Navigator(b)
    
    lcd_print("Press to start.")
    
    b.wait_button()
    
    lcd_print("Started!")
    
    b.move_follow_line(b.stop_if_line, degrees=354.06519295616334)
    
    lcd_print("Reading barcode...")
    
    bs = bar_code(b)
    
    lcd_print(bs)
    
    b.move_follow_line(b.stop_if_line)  # TODO: Remove one?
    b.move_follow_line(b.stop_if_line)
    
    # Move to target position
    path, fin_state = find_path('a3f', bs)
    b.move_for_degrees(140)
    n.move(path)
    
    # Celebrate/indicate that target reached
    lcd_blink()
    
    # Come back to initial position 'a3'
    Config.edges = {}
    path, fin_state = find_path(fin_state, 'a3')
    lcd_print('Returning to base')
    n.move(path)
    n.move({
        'b' : '',
        'r' : 'r',
        'l' : 'l'}[fin_state[2]])
    # Return to base: follow line, pass through bar code, follow line, enter base
    b.move_follow_line(b.stop_if_line, degrees=354.06519295616334)
    b.move_for_degrees(505)
    b.move_follow_line(b.stop_if_line)
    b.move_for_degrees(360)
    
    # Celebrate/indicate that base reached
    lcd_print("I'm at base!!!")

finally: 
    b.reset_all()
    lcd.clear()

