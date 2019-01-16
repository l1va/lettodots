# -*- coding: utf-8 -*-
from alphabet import alphabet
import sys


def convert(msgs, fontx=30, fonty=30, spacex=5, spacey=10, up=5):
    x = 0
    y = 0
    z = 1 * up
    res = [(x, y, z)]

    for msg in msgs:
        msg = msg.upper()
        x = 0
        for character in msg:
            if character in alphabet:
                letter = alphabet[character]
                for dot in letter:
                    res.append((x + dot[0] * fontx, y + dot[1] * fonty, dot[2] * up))
                x += fontx
            else:
                print("not in the alphabet: ", character)
            if character == " ":
                x += fontx
            x += spacex
        y -= fonty + spacey
    return res


def main():
    msgs = ["Hello world!", u"Russian: Привет мир", "subscribe!"]

    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
        msgs = [msg]

    dots = convert(msgs)

    with open("output.txt", 'w') as f:
        for x, y, z in dots:
            f.write("{:.5}\t{:.5}\t{:.5}\n".format(float(x), float(y), float(z)))

    print("Result was printed to output.txt. Done!")


if __name__ == '__main__':
    main()
