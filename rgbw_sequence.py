import time, random
import board
import neopixel

def main():
    pixelPin = board.D18
    numPixels = 100
    ORDER = neopixel.RGB
    sleepTime = 1

    pixels = neopixel.NeoPixel(
        pixelPin, numPixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )

    colors = [ [255, 0, 0],      # red
               [0, 255, 0],      # green
               [0, 0, 255],      # blue 
               [255, 255, 255] ] # white

    try:
        turnOnLed(pixels, numPixels, sleepTime, colors)

    except:
        pixels.fill((0, 0, 0)) # turn off all LEDs
        pixels.show()


def turnOnLed(pixels, numPixels, sleepTime, colors):
    startPos = 0

    while True:
        for i in range(numPixels):
            pos = (startPos + i)%numPixels

            colorNum = pos%len(colors)
            rgb = (colors[colorNum][0], colors[colorNum][1], colors[colorNum][2])
            pixels[i] = rgb

        pixels.show()
        time.sleep(sleepTime)

        if startPos < numPixels - 1:
            startPos += 1
        else:
            startPos = 0


if __name__ == "__main__":
    main()
