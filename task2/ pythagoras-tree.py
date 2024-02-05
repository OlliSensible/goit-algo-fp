import turtle

def draw_square(t, size, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def draw_pythagoras_tree(t, size, level, depth=0):
    color = "#%02x%02x%02x" % (min(255, 100 + depth * 15), 
                               max(0, 255 - depth * 10), 
                               min(255, 100 + depth * 5))  
    if level == 0:
        draw_square(t, size, color)
    else:
        draw_square(t, size, color)
        t.forward(size)
        t.left(45)
        draw_pythagoras_tree(t, size / (2**0.5), level - 1, depth + 1)
        t.right(90)
        t.forward(size / (2**0.5))
        draw_pythagoras_tree(t, size / (2**0.5), level - 1, depth + 1)
        t.left(45)
        t.backward(size)

def main():
    
    try:
        level = int(input("Введіть рівень рекурсії (додатне ціле число): "))
        if level < 0:
            raise ValueError()
    except ValueError:
        print("Будь ласка, введіть додатне ціле число.")
        exit()
    size = 80 
    
    turtle.speed(0)
    turtle.bgcolor("#192a32")
    turtle.penup()
    turtle.goto(-50, -200)
    turtle.pendown()
    turtle.left(90)

    draw_pythagoras_tree(turtle, size, level)
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()