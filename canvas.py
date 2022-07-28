import turtle
import time
# creating turtle pen
t = turtle.Turtle()
  
# taking input for the no of the sides of the polygon
# n = int(input("Enter the no of the sides of the polygon : "))
n=80

# taking input for the length of the sides of the polygon
# l = int(input("Enter the length of the sides of the polygon : "))
l=1
  
  
for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
    # time.sleep(1)
    
