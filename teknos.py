import turtle

#Ablak

ablak = turtle.Screen()
ablak.setup(width=800, height=600)
ablak.bgcolor("black")
ablak.title("PONG")
ablak.tracer(0)

#Bal oldali ütő
bal_uto = turtle.Turtle()
bal_uto.speed(0)
bal_uto.shape("square")
bal_uto.shapesize(stretch_wid=5, stretch_len=1)
bal_uto.color("blue")
bal_uto.penup() 
bal_uto.goto(-350,0)


#Jobb oldali ütő
jobb_uto = turtle.Turtle()
jobb_uto.speed(0)
jobb_uto.shape("square")
jobb_uto.shapesize(stretch_wid=5, stretch_len=1)
jobb_uto.color("red")
jobb_uto.penup() 
jobb_uto.goto(350,0)


#Labda
Labda = turtle.Turtle()
Labda.speed(0)
Labda.shape("circle")
Labda.color("yellow")
Labda.penup()
Labda.goto(0,0)
Labda.változásX = 0.2
Labda.változásY = 0.2

# Pontszám

jobb_pontszam = 0
bal_pontszam = 0

pontszam = turtle.Turtle()
pontszam.speed(0)
pontszam.color("green")
pontszam.penup()
pontszam.hideturtle()
pontszam.goto(0,260)
pontszam.write(f"{bal_pontszam} - {jobb_pontszam}", align = "center", font = ("Curier", 24, "normal"))

def bal_uto_fel():
    y = bal_uto.ycor()
    y += 30
    bal_uto.sety(y)

def bal_uto_le():
    y = bal_uto.ycor()
    y -= 30
    bal_uto.sety(y)

def jobb_uto_fel():
    y = jobb_uto.ycor()
    y += 30
    jobb_uto.sety(y)

def jobb_uto_le():
    y = jobb_uto.ycor()
    y -= 30
    jobb_uto.sety(y)

ablak.onkey(bal_uto_fel, "w")
ablak.onkey(bal_uto_le, "s")
ablak.onkey(jobb_uto_fel, "Up")
ablak.onkey(jobb_uto_le, "Down")
ablak.listen()



#ablak.exitonclick()
while True:

    #a képernyő frissítése
    ablak.update()

    Labda.setx(Labda.xcor() + Labda.változásX)
    Labda.sety(Labda.ycor() + Labda.változásY)

    # tetejéröl pattanjon vissza
    if Labda.ycor() > 288 :
        Labda.sety(288)
        Labda.változásY *= -1

    #aljáról pattanjon vissza:
    if Labda.ycor() < -288:
        Labda.sety(-288)
        Labda.változásY *= -1 

    #jobb oldal érintése
    if Labda.xcor() > 388:
        Labda.goto(0,0)
        Labda.változásX *= -1
        bal_pontszam += 1
        pontszam.clear()
        pontszam.write(f"{bal_pontszam} - {jobb_pontszam}", align = "center", font = ("Curier", 24, "normal"))


    #bal oldal érintése
    if Labda.xcor() < -388:
        Labda.goto(0,0)
        Labda.változásX *= -1
        jobb_pontszam += 1
        pontszam.clear()
        pontszam.write(f"{bal_pontszam} - {jobb_pontszam}", align = "center", font = ("Curier", 24, "normal"))


    #jobb ütő érintése
    if jobb_uto.xcor()-20 < Labda.xcor() < jobb_uto.xcor() and  jobb_uto.ycor() -40 < Labda.ycor() < jobb_uto.ycor() + 40:
        Labda.setx(jobb_uto.xcor()-20)
        Labda.változásX *= -1
        #Labda.változásY *= -1 

    #bal ütő érintése
    if bal_uto.xcor() < Labda.xcor() < bal_uto.xcor() + 20 and  bal_uto.ycor() -40 < Labda.ycor() < bal_uto.ycor() + 40:
        Labda.setx(bal_uto.xcor()+20)
        Labda.változásX *= -1
        #Labda.változásY *= -1 