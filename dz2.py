import turtle
import argparse

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3)  # Starting point for a better snowflake position
    t.pendown()

    # Draw the three sides of the snowflake
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Draw a Koch snowflake with a specified recursion level.")
    parser.add_argument("order", type=int, help="Recursion level of the Koch snowflake.")
    args = parser.parse_args()

    draw_koch_snowflake(args.order)

if __name__ == "__main__":
    main()
