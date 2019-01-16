from alphabet import alphabet
import sys


def convert(msg, fontx=30, fonty=30, space=5, up=5):
    msg = msg.upper()

    x = 0
    y = 0
    z = 1 * up
    res = [(x, y, z)]

    for character in msg:
        if character in alphabet:
            letter = alphabet[character]
            for dot in letter:
                res.append((x + dot[0] * fontx, y + dot[1] * fonty, dot[2] * up))
            x += fontx
        if character == " ":
            x += fontx
        x += space
    return res


def main():
    msg = "Hello world!"

    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])

    dots = convert(msg)

    with open("output.txt", 'w') as f:
        for x, y, z in dots:
            f.write("{:.5}\t{:.5}\t{:.5}\n".format(float(x),float(y),float(z)))

    print("Result was printed to output.txt. Done!")


main()
