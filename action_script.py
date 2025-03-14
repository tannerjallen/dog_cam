import RPi.GPIO as GPIO
import time
import json

# Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

def beep_dog():
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set the pin as an output pin
    GPIO.setup(config['beep_gpio_pin'], GPIO.OUT, initial=GPIO.LOW)  # Start with pin LOW

    # To turn the transistor ON (set pin HIGH)
    GPIO.output(config['beep_gpio_pin'], GPIO.HIGH)
    print(f"GPIO{config['beep_gpio_pin']} is HIGH, transistor ON")

    # Wait for the specified duration
    time.sleep(config['duration'])

    # To turn the transistor OFF (set pin LOW)
    GPIO.output(config['beep_gpio_pin'], GPIO.LOW)
    print(f"GPIO{config['beep_gpio_pin']} is LOW, transistor OFF")

    # Clean up GPIO settings after use
    GPIO.cleanup()
    print("Beeped dog.")
    return

def buzz_dog():
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set the pin as an output pin
    GPIO.setup(config['buzz_gpio_pin'], GPIO.OUT, initial=GPIO.LOW)  # Start with pin LOW

    # To turn the transistor ON (set pin HIGH)
    GPIO.output(config['buzz_gpio_pin'], GPIO.HIGH)
    print(f"GPIO{config['buzz_gpio_pin']} is HIGH, transistor ON")

    # Wait for the specified duration
    time.sleep(config['duration'])

    # To turn the transistor OFF (set pin LOW)
    GPIO.output(config['buzz_gpio_pin'], GPIO.LOW)
    print(f"GPIO{config['buzz_gpio_pin']} is LOW, transistor OFF")

    # Clean up GPIO settings after use
    GPIO.cleanup()
    return
