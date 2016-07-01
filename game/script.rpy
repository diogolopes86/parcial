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
define k = Character('Krusty', color="#cfff26")
define m = Character('Moe', color="#88ff88")
define n = Character('Milhouse', color="#ff98cc")
define c = Character('Guardia Clansy', color="#2298ff")

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
image krusty = "krusty.png"
image moe = "moe.png"
image milhouse = "milhouse.png"
image detective hablando = im.FactorScale("detective_hablando.png", 0.6)
image detective pruebas = im.FactorScale("detective_pruebas.png", 0.5)
image detective aha = im.FactorScale("detective_aha.png", 0.5)
image detective pensando = im.FactorScale("detective_pensando.png", 0.5)
image homer triste = "homer_triste.png"

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
    d "A quien usted vio fuera del pueblo?"

    python:
        from pyswip import Prolog
        prolog = Prolog()
        prolog.consult('/home/diogo/Documentos/simpsons.pl')
        asesino = list(prolog.query('murderer(X)'))
        new_prolog_code = open('/home/diogo/Documentos/murder.pl','w')
        new_facts = []

    menu:

      "Homer":
        python:
          new_facts.append('murderer(homer).')
        $ gift = "homer"
        jump homer
      "Bart":
        python:
          new_facts.append('murderer(bart).')
        $ gift = "bart"
        jump bart
      "Flanders":
        python:
          new_facts.append('murderer(flanders).')
        $ gift = "flanders"
        jump flanders



    label homer:
      scene bg sala
      show krusty:
        xalign 0.5 yalign 0.5
      k "Yo vi Homer saliendo del pueblo con la victima"

      hide krusty
      show detective pensando:
        xalign 0.5 yalign 0.5
      d "Mmmm interesante..."

      hide detective pensando
      show krusty:
        xalign 0.5 yalign 0.5
      k "Los segui y vi que entraron en un restaurante cerca de la carretera"
      k "Despues de un tiempo, Homer saliendo solo de adentro"

      hide krusty
      show detective pensando:
        xalign 0.5 yalign 0.5
      d "Todo indica que tenia un cumplice"
      d "Gracias por su testimonio"

      hide detective pensando
      show detective pruebas:
        xalign 0.5 yalign 0.5
      d "Bien, creo que no me resta otra"

      python:
        new_set_of_facts = list(set(new_facts))
        for x in new_set_of_facts:
          new_prolog_code.write(x)
        new_prolog_code.close()
        prolog2 = Prolog()
        prolog2.consult('/home/diogo/Documentos/murder.pl')
        asesino = list(prolog2.query('murderer(X)'))
        d("Guardia Clansy, el asesino es %s"%asesino[0]['X'])

      hide detective pruebas
      show detective aha:
        xalign 0.5 yalign 0.5
      d "DETENGA A HOMER"

      hide detective aha
      show policia:
        xalign 0.5 yalign 0.5dd
      c "NO TE MUEVAS MALIANTE"

      hide policia
      show homer triste:
        xalign 0.5 yalign 0.5
      h "Nunca pense que me descobririan"
      return


    label bart:
      scene bg sala
      show milhouse:
        xalign 0.5 yalign 0.5
      n "Yo vi Bart saliendo del pueblo con la victima"

      hide milhouse
      show detective pensando:
        xalign 0.5 yalign 0.5
      d "Mmmm interesante..."

      hide detective pensando
      show milhouse:
        xalign 0.5 yalign 0.5
      n "Los segui y vi que entraron en un restaurante cerca de la carretera"
      n "Despues de un tiempo, Bart regreso al pueblo solo en el carro de la victima"

      hide milhouse
      show detective pensando:
        xalign 0.5 yalign 0.5
      d "Todo indica que tenia un cumplice"
      d "Gracias por su testimonio"

      hide detective pensando
      show detective pruebas:
        xalign 0.5 yalign 0.5
      d "Bien, creo que no me resta otra"

      python:
        new_set_of_facts = list(set(new_facts))
        for x in new_set_of_facts:
          new_prolog_code.write(x)
        new_prolog_code.close()
        prolog2 = Prolog()
        prolog2.consult('/home/diogo/Documentos/murder.pl')
        asesino = list(prolog2.query('murderer(X)'))
        d("Guardia Clansy, el asesino es %s"%asesino[0]['X'])

      hide detective pruebas
      show detective aha:
        xalign 0.5 yalign 0.5
      d "DETENGA A BART"

      hide detective aha
      show policia:
        xalign 0.5 yalign 0.5
      c "QUEDAS ARRESTADO"

      hide policia
      show bart2:
        xalign 0.5 yalign 0.5
      h "Imposible, ese plan era perfecto"
      return


    label flanders:
      scene bg sala
      show moe:
        xalign 0.5 yalign 0.5
      m "Yo vi Flanders saliendo del pueblo con la victima"

      hide moe
      show detective pensando:
        xalign 0.5 yalign 0.5
      d "Mmmm interesante..."

      hide detective pensando
      show moe:
        xalign 0.5 yalign 0.5
      m "Los segui y vi que entraron en un restaurante cerca de la carretera"
      m "Despues de un tiempo, no se supo mas de la victima y flandes regreso solo al pueblo"

      hide moe
      show detective pensando:
        xalign 0.5 yalign 0.5
      d "Todo indica que tenia un cumplice"
      d "Gracias por su testimonio"

      hide detective pensando
      show detective pruebas:
        xalign 0.5 yalign 0.5
      d "Bien, creo que no me resta otra"

      python:
        new_set_of_facts = list(set(new_facts))
        for x in new_set_of_facts:
          new_prolog_code.write(x)
        new_prolog_code.close()
        prolog2 = Prolog()
        prolog2.consult('/home/diogo/Documentos/murder.pl')
        asesino = list(prolog2.query('murderer(X)'))
        d("Guardia Clansy, el asesino es %s"%asesino[0]['X'])

      hide detective pruebas
      show detective aha:
        xalign 0.5 yalign 0.5
      d "DETENGA A FLANDERS"

      hide detective aha
      show policia:
        xalign 0.5 yalign 0.5
      c "NO TE MUEVAS TODO LO QUE DIGAS PUEDE SER UTILIZADO EN TU CONTRA"

      hide policia
      show flanders2:
        xalign 0.5 yalign 0.5
      h "Yo no imaginaba que habia un testigo"


return
