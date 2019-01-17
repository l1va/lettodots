# -*- coding: utf-8 -*-
from alphabet import alphabet
import sys


def convert(msgs, fontx=20, fonty=20, spacex=3, spacey=8, up=5):
    x = 0
    y = 0
    z = 1 * up
    res = [(x, y, z)]

    for msg in msgs:
        msg = msg.upper()
        x = 0
        for character in msg:
            if character == " ":
                x += fontx
                continue
            if character in alphabet:
                letter = alphabet[character]
                for dot in letter:
                    res.append((x + dot[0] * fontx, y + dot[1] * fonty, dot[2] * up))
                x += fontx
            else:
                print("not in the alphabet: ", character)

            x += spacex
        y -= fonty + spacey
    return res


def main():
    # msgs = ["Hello world!", u"Russian: Привет мир", "subscribe!"]

    msgs = [u"Я был бы несчастливейшим",
            u"из людей, ежели бы я",
            u"не нашел цели для моей",
            u"жизни - цели общей и полезной.",
            u"Теперь же жизнь моя будет вся",
            u"стремлением деятельным и",
            u"постоянным к этой одной цели."]

    # msgs = [u"Один,", u"Два"]

    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
        msgs = [msg]

    dots = convert(msgs, fontx=10, fonty=10, spacey=4)

    with open("output.csv", 'w') as f:
        for x, y, z in dots:
            f.write("{:.5},{:.5},{:.5}\n".format(float(x), float(y), float(z)))

    print("Result has been printed to output.csv. Done!")


if __name__ == '__main__':
    main()
