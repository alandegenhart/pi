"""GIPO test script"""

# Imports
import time
import gpiozero


def main():
    """Main display function."""
    led = gpiozero.LED(17)

    # Turn on and off LED
    for i in range(10):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

    return None


if __name__ == '__main__':
    main()
