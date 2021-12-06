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
    button = gpiozero.Button(17)
    relay_pins = [18, 23, 24, 25, 12, 16, 20, 21]
    relay_array = [Relay(pin, id) for pin, id in enumerate(relay_pins)]

    # Turn on and off LED
    for i in range(len(relay_array)):
        relay_array[i].toggle()
        time.sleep(1)
        relay_array[i].toggle()

    # Initialize button action
    #button.when_pressed = relay.toggle

    #signal.pause()

    return None


if __name__ == '__main__':
    main()
