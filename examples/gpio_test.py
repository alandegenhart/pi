"""GIPO test script"""

# Imports
import time
import gpiozero


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
    while True:
        if button.is_pressed:
            button_state = 'pressed'
        else:
            button_state = 'not pressed'

        print(f'Button state: {button_state}')

    return None


if __name__ == '__main__':
    main()
