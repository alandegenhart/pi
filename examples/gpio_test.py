"""GIPO test script"""

# Imports
import time
import gpiozero
import signal


class Relay():
    def __init__(self, pin, id):
        self.line = gpiozero.DigitalOutputDevice(pin)
        self.id = id  # ID of the relay
        self.is_off = True  # Relay state

    def toggle(self):
        """Toggle relay state"""
        if self.is_off:
            # Turn relay ON
            self.line.on()
            print(f'Relay {self.id} set to ON')
            self.is_off = False  # Update state of relay
        else:
            # Turn relay OFF
            self.line.off()
            print(f'Relay {self.id} set to OFF')
            self.is_off = True

def main():
    """Main display function."""
    button = gpiozero.Button(22)
    relay = Relay(17, 0)

    # Turn on and off LED
    for i in range(4):
        relay.toggle()
        time.sleep(0.25)

    # Initialize button action
    button.when_pressed = relay.toggle

    signal.pause()

    return None


if __name__ == '__main__':
    main()
