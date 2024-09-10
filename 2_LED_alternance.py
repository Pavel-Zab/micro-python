import time
led_verte = pyb.Pin( 'X1', pyb.Pin.OUT_PP)
led_verte.high()
led_rouge = pyb.Pin( 'X3', pyb.Pin.OUT_PP)
led_rouge.high()

while True:
    led_verte.on()
    time.sleep(1)
    led_verte.off()
    time.sleep(0.05)
    led_rouge.on()
    time.sleep(1)
    led_rouge.off()
    time.sleep(0.05)
