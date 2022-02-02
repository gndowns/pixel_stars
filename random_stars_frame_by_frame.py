from random import randint
import os

import curses

from drawille import animate
from drawille import Canvas


# Uncomment for purple background?
#  stdscr = curses.initscr()
#  stdscr.refresh()


def data_yielder(height, width):
    while True:
        data = []

        star_centers = []
        for y in range(height):
            for x in range(width):
                if randint(1, 2000) > 1999:
                    star_centers.append((x,y))
                    data.append((x,y))

        for x, y in star_centers:
            # the main "cross" of the star
            x_min = max(0, x-4)
            y_min = max(0, y-4)
            x_max = min(width, x+5)
            y_max = min(height, y+5)

            for xp in range(x_min, x_max):
                data.append((xp, y))
            for yp in range(y_min, y_max):
                data.append((x, yp))

            # The filled in center square of the star
            x_min = max(0, x-1)
            y_min = max(0, y-1)
            x_max = min(width, x+2)
            y_max = min(height, y+2)
            for xp in range(x_min, x_max):
                for yp in range(y_min, y_max):
                    data.append((xp, yp))

        yield data


def main():
    canvas = Canvas()

    term_width, term_height = os.get_terminal_size()

    animate(canvas, data_yielder, 1. / 60, term_height*4-4, term_width*2-2)


if __name__ == "__main__":
    main()
