import time, random, colorsys
import board
import neopixel

def main():
    pixel_pin = board.D18
    num_pixels = 100
    ORDER = neopixel.RGB # RGB
    sleepTime = 0

    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )

    try:
        rainbow = rainbowGenerator()
        while True:
            pixels.fill(next(rainbow))
            pixels.show()
            time.sleep(sleepTime)

    except:
        pixels.fill((0, 0, 0)) # turn off all LEDs
        pixels.show()


def rainbowGenerator():
    hue = 0.0
    step = 1/256

    while True:
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        rgbTuple = tuple(int(x * 255) for x in rgb)
        ##print(rgbTuple)
        yield rgbTuple

        hue = (hue + step) % 1.0


if __name__ == "__main__":
    main()
