# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define h = Character('Homer', color="#c8ffc8")
define d = Character('Detective Clansy', color="#88ff25")

image bg springfield = "springfield.jpg"
image bg cadeia = "cadeia4.jpg"
image sala = "sala3.jpg"
image homer = im.FactorScale("homer.png", 1.15)
image homer2 = "homer2.png"
image bart = im.FactorScale("bart.png", 1.15)
image bart2 = "bart2.png"
image burns = "burns.png"
image burns2 = "burns2.png"
image flanders = "flanders.png"
image flanders2 = "flanders2.png"
image policia = "policia.png"
image policia2 = "policia2.png"
image policia3 = "policia3.png"

# The game starts here.
# - El juego comienza aquí.
label start:

    scene bg springfield
    show policia3:
      xalign 0.5 yalign 0.5
    d "Encontraron una mujer muerta fuera del pueblo."
    d "Testigos dicen haber escuchado disparos y alguien corriendo." 

    hide policia3
    show policia2:
      xalign 0.5 yalign 0.5
    d "Aqui tenemos los sospechosos."

    hide policia2
    show homer
    d "Ese es Homer"

    hide homer
    show bart
    d "Tenemos a Bart"

    hide bart
    show flanders:
        xalign 0.5 yalign 0.2
    d "Sr. Flanders"

    hide flanders
    show burns
    d "Y por ultimo, pero no menos importante, Sr. Burns"

    return
