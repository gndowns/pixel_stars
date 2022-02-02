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
        for y in range(height):
            for x in range(width):
                if randint(1, 1000) > 999:
                    data.append((x,y))

        yield data


def main():
    canvas = Canvas()

    term_width, term_height = os.get_terminal_size()

    animate(canvas, data_yielder, 1. / 60, term_height*4-4, term_width*2-2)


if __name__ == "__main__":
    main()
