import time, random
import board
import neopixel

def main():
    pixel_pin = board.D18
    num_pixels = 100
    ORDER = neopixel.RGB
    sleepTime = 0.01

    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )

    colors = [ [255, 0, 0],   # red
               [255, 165, 0], # orange
               [255, 255, 0], # yellow
               [0, 128, 0],   # green
               [0, 255, 255], # cyan
               [0, 0, 255],   # blue
               [128, 0, 128] ]# purple

    step = 100

    try:
        while True:
            for i in range(len(colors)):
                for j in range(step):
                    r = int(colors[i][0]*(j+1)/step)
                    g = int(colors[i][1]*(j+1)/step)
                    b = int(colors[i][2]*(j+1)/step)
                    #print(r, g, b)

                    pixels.fill((r, g, b))
                    pixels.show()
                    time.sleep(sleepTime)

    except:
        pixels.fill((0, 0, 0)) # turn off all LEDs
        pixels.show()


if __name__ == "__main__":
    main()
