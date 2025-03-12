import RPi.GPIO as GPIO
import time

def beep_dog():
        # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set GPIO20 as an output pin
    GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)  # Start with GPIO20 LOW

    # To turn the transistor ON (set GPIO20 HIGH)
    GPIO.output(20, GPIO.HIGH)
    print("GPIO20 is HIGH, transistor ON")

    # Wait for 2 seconds (for demonstration purposes)
    time.sleep(.2)

    # To turn the transistor OFF (set GPIO20 LOW)
    GPIO.output(20, GPIO.LOW)
    print("GPIO20 is LOW, transistor OFF")

    # Clean up GPIO settings after use
    GPIO.cleanup()
    print("Beeped dog.")
    return

def buzz_dog():
        # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Set GPIO20 as an output pin
    GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)  # Start with GPIO20 LOW

    # To turn the transistor ON (set GPIO20 HIGH)
    GPIO.output(21, GPIO.HIGH)
    print("GPIO20 is HIGH, transistor ON")

    # Wait for 2 seconds (for demonstration purposes)
    time.sleep(.2)

    # To turn the transistor OFF (set GPIO20 LOW)
    GPIO.output(21, GPIO.LOW)
    print("GPIO20 is LOW, transistor OFF")

    # Clean up GPIO settings after use
    GPIO.cleanup()
    return
