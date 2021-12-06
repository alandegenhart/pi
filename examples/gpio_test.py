"""GIPO test script"""

# Imports
import time
import gpiozero
import signal


class Relay():
    def __init__(self, pin):
        self.led = gpiozero.LED(pin)

    def on():
        """Turn on LED."""
        self.led.on()

    def off():
        """Turn off LED."""
        self.led.off()


def main():
    """Main display function."""
    led = gpiozero.LED(17)
    button = gpiozero.Button(22)
    relay = Relay(17)

    # Turn on and off LED
    for i in range(5):
        led.on()
        time.sleep(0.25)
        led.off()
        time.sleep(0.25)

    # Initialize button action
    button.when_pressed = relay.on
    button.when_released = relay.off

    signal.pause()

    return None


if __name__ == '__main__':
    main()
