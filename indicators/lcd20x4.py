from RPLCD.i2c import CharLCD
import time

lcd = CharLCD('PCF8574', 0x27)

#lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1,
#              cols=20, rows=4, dotsize=8,
#              charmap='A02',
#             auto_linebreaks=True,
#              backlight_enabled=True)
lcd.clear()
lcd.backlight_enabled = True
time.sleep(0.1)
lcd.backlight_enabled = False
time.sleep(0.1)
lcd.backlight_enabled = True
time.sleep(0.1)
lcd.backlight_enabled = False
time.sleep(0.1)
lcd.backlight_enabled = True
time.sleep(0.1)
#lcd.display_enabled = True
lcd.home()
#lcd.cursor_pos = (2, 2)
print("BL disabled")
for i in range(10000000):
    #lcd.home()
    lcd.cursor_pos = (2, 2)
    lcd.write_string(u'Hello!!!' + str(i))
    #lcd.crlf()
    time.sleep(0.2)
lcd.clear()
#lcd.cursor_pos = (2, 0)
#lcd.write_string('https://github.com/\n\rdbrgn/RPLCD')

#time.sleep(100.)
#lcd.backlight_enabled = False