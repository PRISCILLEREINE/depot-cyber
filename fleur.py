import turtle

t = turtle.Turtle()
t.speed(0)  
turtle.bgcolor("white") 

couleurs = ["purple", "blue", "teal", "green", "orange", "red", "magenta"]

def dessiner_motif(taille):
  t.circle(taille, 60)
  t.left(120)
  t.circle(taille, 60)
  t.left(120)

nombre_repetitions = 60
angle_rotation = 360 / nombre_repetitions

for i in range(nombre_repetitions):
  t.color(couleurs[i % len(couleurs)])

  dessiner_motif(100)

  t.left(angle_rotation)

t.hideturtle()

turtle.done() 