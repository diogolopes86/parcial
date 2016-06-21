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
define b = Character('Bart', color="#c8cc00")
define f = Character('Flanders', color="#c0ccff")
define d = Character('Detective', color="#88ff25")

image bg springfield = "springfield.jpg"
image bg cadeia = "cadeia4.jpg"
image bg sala = "sala3.jpg"
image homer = im.FactorScale("homer.png", 1.15)
image homer2 = "homer2.png"
image bart = im.FactorScale("bart.png", 1.15)
image bart2 = "bart2.png"
image flanders = "flanders.png"
image flanders2 = "flanders2.png"
image policia = "policia.png"
image policia2 = "policia2.png"
image policia3 = "policia3.png"
image detective hablando = im.FactorScale("detective_hablando.png", 0.6)
image detective hablando pruebas = im.FactorScale("detective_pruebas.png", 0.5)
image detective hablando aha = im.FactorScale("detective_aha.png", 0.5)

# The game starts here.
# - El juego comienza aquí.
label start:

    scene bg springfield
    show detective hablando:
      xalign 0.5 yalign 0.5
    d "Encontraron una mujer muerta fuera del pueblo."
    d "Un testigos dice haber escuchado disparos y alguien corriendo." 
    d "Aqui tenemos los sospechosos."

    hide detective hablando
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
    show policia3:
        xalign 0.5 yalign 0.5
    d "Vamos guardia Clansy, traeme el testigo"
    d "Vamos a las preguntas:"
    d "Quien usted vio afuera del pueblo?"

    menu:

      "Homer":
        jump homer
      "Bart":
        jump bart
      "Flanders":
        jump flanders

    label homer:
      scene bg sala
      show homer2:
        xalign 0.5 yalign 0.8

      hide homer2
      show detective hablando:
        xalign 0.5 yalign 0.5
      d "Viste Homer junto con la victima?"

      menu:
    
        "Si":
          jump si
        "No":
          jump no
      label no:
        d "Entonces usted no sabe nada. ¡Caso archivado!"
        return
      label si:
        show detective pruebas:
          xalign 0.5 yalign 0.5
        d "Interesante, eso quiere decir mucha cosa."

return
