def mangekant(lines, color, lengde):
    import turtle
    turtle.color(color)
    turtle.begin_fill()
    for n in range(lines):
        turtle.left(360/lines)
        turtle.forward(lengde)
    turtle.end_fill()
    turtle.done()
