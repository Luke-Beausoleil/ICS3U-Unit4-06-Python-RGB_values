#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program returns all possible RGB values


def main():
    # this function outputs the RGB values

    # variables
    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                print("RGB({0}, {1}, {2})".format(red, green, blue))
                blue += 1
            green += 1
        red += 1


if __name__ == "__main__":
    main()
