import turtle
import math


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)


if __name__ == '__main__':
    bob = turtle.Turtle()
    draw(bob, 3, 5)
    turtle.mainloop()
