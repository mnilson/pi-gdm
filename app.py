from flask import Flask
from gpiozero import LED
app = Flask(__name__)

#led = LED(17)

def flash_led(num):
	for i in range(num):
		led.on()
		sleep(1)
		led.off()
		sleep(1)

@app.route('/')
def hello_world():
	flash_led(5)
	return 'Hello, World'

if __name__ == '__main__':
	app.run()




