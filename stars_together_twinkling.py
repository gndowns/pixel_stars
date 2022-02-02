import random
import os

import curses

from drawille import animate
from drawille import Canvas


# Uncomment for purple background?
#  stdscr = curses.initscr()
#  stdscr.refresh()


# Moves at every stage
random.seed(1492)


def data_yielder(height, width):
    star_centers = []
    for y in range(height):
        for x in range(width):
            #  if randint(1, 5000) > 4999:
            if random.randint(1, 1000) > 999:
                star_centers.append((x,y))

    stage = 0

    while True:
        data = []

        if stage == 0:
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

        elif stage == 1:
            for x, y in star_centers:
                # the main "cross" of the star
                x_min = max(0, x-5)
                y_min = max(0, y-5)
                x_max = min(width, x+6)
                y_max = min(height, y+6)

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

        elif stage == 2:
            for x, y in star_centers:
                # the main "cross" of the star
                x_min = max(0, x-6)
                y_min = max(0, y-6)
                x_max = min(width, x+7)
                y_max = min(height, y+7)

                for xp in range(x_min, x_max):
                    data.append((xp, y))
                for yp in range(y_min, y_max):
                    data.append((x, yp))

                x_min_min = max(0, x_min -2)
                y_min_min = max(0, y_min - 2)
                x_max_max = min(width-1, x_max + 2)
                y_max_max = min(height-1, y_max + 2)

                data.append((x, y_min_min))
                data.append((x, y_max_max))
                data.append((x_min_min, y))
                data.append((x_max_max, y))

                # The filled in center square of the star
                x_min = max(0, x-1)
                y_min = max(0, y-1)
                x_max = min(width, x+2)
                y_max = min(height, y+2)
                for xp in range(x_min, x_max):
                    for yp in range(y_min, y_max):
                        data.append((xp, yp))

        stage += 1
        stage = stage % 3

        yield data


def main():
    canvas = Canvas()

    term_width, term_height = os.get_terminal_size()

    animate(canvas, data_yielder, 1, term_height*4-4, term_width*2-2)


if __name__ == "__main__":
    main()
