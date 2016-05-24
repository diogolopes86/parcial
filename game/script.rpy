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
define d = Character('Detective', color="#88ff25")

image bg ciudad = "ciudad.png"
image bg cadeia = "cadeia4.jpg"
image sala = "sala3.jpg"
image homer = im.FactorScale("homer.png",0.8)
image barney = "barney.png"
image barney2 = "barney2.png"
image barney3 = "barney3.png"
image bart = "bart.png"
image bart2 = "bart2.png"
image bob = "bob.png"
image bob2 = "bob2.png"
image burns = "burns.png"
image chef = "chef_clancy.png"
image flanders = "flanders.png"
image marge = "marge.png"
image marge2 = "marge2.png"
image detective hablando = "detective_hablando.png"
image detective piensando = "detective_piensando.png"
image detective aha = "detective_aha.png"
image detective pruebas = "detective_pruebas.png"

# The game starts here.
# - El juego comienza aquí.
label start:

    scene bg ciudad
    show detective hablando:
      xalign 0.8 yalign 0.7
    d "Encontraron una mujer muerta fuera del pueblo."
    d "Testigos dicen haber escuchado disparos y alguien corriendo." 

    d "Aqui tenemos los sospechosos."

    hide detective hablando
    show homer
    d "Ese es Homer"

    hide homer
    show barney2
    d "Tenemos a Barney"

    hide barney2
    show bart2
    d "Ese es Bart"

    hide bart2
    show bob
    d "Bob"

    hide bob
    show burns
    d "El sr. Burns"

    hide burns
    show flanders
    d "Sr. Flanders"

    hide flanders
    show chef
    d "Y por ultimo, pero no menos importante, Moe"

    return
