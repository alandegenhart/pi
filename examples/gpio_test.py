"""GIPO test script"""

# Imports
import time
import gpiozero
import signal


def main():
    """Main display function."""
    led = gpiozero.LED(17)
    button = gpiozero.Button(22)

    # Turn on and off LED
    for i in range(5):
        led.on()
        time.sleep(0.25)
        led.off()
        time.sleep(0.25)

    # Test button
    button.when_pressed = led.on
    button.when_released = led.off

    signal.pause()

    return None


if __name__ == '__main__':
    main()
