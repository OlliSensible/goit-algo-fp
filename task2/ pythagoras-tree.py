import sys
import turtle
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def draw_pythagoras_tree(turtle, length, angle, level):
    if level == 0:
        turtle.forward(level)
    else:
        turtle.forward(length)
        turtle.left(angle)
        draw_pythagoras_tree(turtle, length * 0.7, angle, level - 1)
        turtle.right(2 * angle)
        draw_pythagoras_tree(turtle, length * 0.7, angle, level - 1)
        turtle.left(angle)
        turtle.backward(length)

def get_recursion_level():
    while True:
        try:            
            recursion_level = int(input("\nВведіть рівень рекурсії (додатне ціле число): "))
            return recursion_level
        
        except ValueError:
            print("\nБудь ласка, введіть додатне ціле число.")
        
def main():

    recursion_level = get_recursion_level()

    turtle.speed(0)
    turtle.up()
    turtle.left(90)
    turtle.backward(200)
    turtle.down()
    turtle.color("#efc75e")
    turtle.bgcolor("#192a32")
    turtle.pensize(2)

    draw_pythagoras_tree(turtle, 150, 35, recursion_level)
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()