# -*- coding: utf-8 -*-
from alphabet import alphabet
import sys
import math


def convert(msgs, fontx=20, fonty=20, spacex=3, spacey=8, up=5, shift=True):
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
                if shift:
                    x += fontx
            else:
                print("not in the alphabet: ", character)
            if character == " " and shift:
                x += fontx
            if shift:
                x += spacex
        if shift:
            y -= fonty + spacey
    return res
    
def matZYX(rx,ry,rz):
    ca, cb, cc = math.cos(rz), math.cos(ry), math.cos(rx)
    sa, sb, sc = math.sin(rz), math.sin(ry), math.sin(rx)
    # rotation matrix Z-Y-X	
    return [[ca*cb, ca*sb*sc-sa*cc, sa*sc+ca*sb*cc],
            [sa*cb, sa*sb*sc+ca*cc, sa*sb*cc-ca*sc],
            [  -sb,          cb*sc,          cb*cc]]

# points : get after conversation
# translation : [dx,dy,dz]
# rotation : [rotZ,rotY,rotX]            
def transform(points, translation, rotation):
    R = matZYX(rotation[0],rotation[1],rotation[2])
    res = []
    for c in points:
        x = R[0][0]*c[0]+R[0][1]*c[1]+R[0][2]*c[2]+translation[0]
        y = R[1][0]*c[0]+R[1][1]*c[1]+R[1][2]*c[2]+translation[1]
        z = R[2][0]*c[0]+R[2][1]*c[1]+R[2][2]*c[2]+translation[2]
        res.append([x,y,z,rotation[0],rotation[1],rotation[2]])
    return res        

def main():
    #msgs = ["Hello world!", u"Russian: Привет мир", "subscribe!"]
        
#    msgs = [u"Я был бы несчастливейшим",
#           u"из людей,ежели бы я",
#           u"не нашел цели для моей",
#           u"жизни - цели общей и",
#           u"полезной. Теперь же жизнь",
#           u"моя будет вся стремлением",
#           u"деятельным и постоянным",
#           u"к этой одной цели.",
#           u"           Л.Н.Толстой"]

    #msgs = [u"Один,", u"Два"]
    
    msgs = ["INNOPOLIS"]

    if len(sys.argv) > 1:
        msg = " ".join(sys.argv[1:])
        msgs = [msg]
        
    FONTY = 200
    FONTX = 300

    dots = convert(msgs,fontx=300,fonty=FONTY,up=-50,shift=False)
    # rotate in xy plane (around Z axis)
    dots = transform(dots, [0,0,0], [0,0,0.5*math.pi])
    # spacial transformation
    dots = transform(dots, [650,-0.5*FONTY,650-0.5*FONTX], [math.pi,math.pi*0.5,math.pi])

    with open("output.csv", 'w') as f:
        for d in dots:
            f.write(",".join(["{:.5}".format(float(i)) for i in d]))
            f.write("\n")

    print("Result has been printed to output.csv. Done!")


if __name__ == '__main__':
    main()
