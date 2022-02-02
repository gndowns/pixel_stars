from random import randint
from time import sleep
import os


def render(data):
    # Escape code to Clear screen,
    # so we can draw new frame.
    print('\033[2J')

    for row in data:
        for val in row:
            char = "o" if val else " "
            print(char, end="")
        print("")


def initialize_data(height, width):
    # Data is an array representing each pixel on the screen. 
    # 1 is "ON", representing a star at that point.
    # 0 is "OFF", representing no star at that point.
    #  data = [[0 for _ in range(width)] for _ in range(height)]
    data = []
    for _ in range(height):
        row = [1 if randint(1, 1000) > 999 else 0 for _ in range(width)]
        data.append(row)

    return data


def main():
    term_width, term_height = os.get_terminal_size()
    data = initialize_data(term_height, term_width)
    
    # Main event loop.
    while True:
        render(data)
        sleep(0.075)


if __name__ == "__main__":
    main()
