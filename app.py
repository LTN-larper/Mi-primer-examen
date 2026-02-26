import streamlit as st

# 1. EL ARCHIVADOR (Nuestra base de datos de preguntas)
# Cada bloque entre { } es una pregunta distinta. Cada pregunta es un diccionario de 3 entradas (texto, opciones, correcta).
# Creamos la lista de preguntas:
preguntas = [
   {
        "texto": "¿Cuál es el lugar más frío de la tierra?",
        "opciones": ["Polo Norte", "Antártida", "Rusia", "Islandia", "Mi casa",],
        "correcta": "Antártida"
    },
    {
        "texto": "¿Quién escribió 'Don Quijote de la Mancha'?",
        "opciones": ["Federico García Lorca", "Miguel de Cervantes", "Gabriel García Márquez", "Pablo Picasso",],
        "correcta": "Miguel de Cervantes"
    },
    {
        "texto": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Misisipi", "Amazonas", "Nilo", "Tajo"],
        "correcta": "Nilo"
    },
    {
        "texto": "¿Qué elemento de la tabla periódica tiene el símbolo 'Og'?",
        "opciones": ["Oro", "Oganeson", "Oxígeno",],
        "correcta": "Oganeson"
    },
    {
        "texto": "¿En qué continente se encuentra el Monte Everest?",
        "opciones": ["Asia", "África", "América", "América del Sur",],
        "correcta": "Asia"
    },
    {
        "texto": "¿Qué planeta es el Planeta Rojo?",
        "opciones": ["Júpiter", "Venus", "Marte", "Saturno",],
        "correcta": "Marte"
    },
    {
        "texto": "¿Componente principal que procesa los datos en un ordenador?",
        "opciones": ["RAM", "Disco Duro", "CPU (Procesador)",],
        "correcta": "CPU (Procesador)"
    },
    {
        "texto": "¿Cual es la marca mas vendida de zapartillas?",
        "opciones": ["Adidas", "Nike", "Reebok", "Puma"],
        "correcta": "Nike"
    },
    {
        "texto": "¿Cuál es el país con más habitantes del mundo actualmente?",
        "opciones": ["China", "Estados Unidos", "India", "Rusia"],
        "correcta": "India"
    }
       
]

# Configuración visual de la página
st.title("🎓 Mi Primer Examen de tuby")
st.write("Responde a las preguntas y pulsa el botón al final para saber tu nota.")

# 2. EL FORMULARIO (Agrupamos todo para que no se recargue la web a cada clic)
# Eso se consigue con el comando with

with st.form("quiz_form"):

    # Aquí guardaremos las respuestas que elija el alumno. Será una lista.
    respuestas_usuario = []
   
    # Recorremos el archivador usando un bucle 'for' para crear las preguntas
    for pregunta in preguntas:
        st.subheader(pregunta["texto"]) # Ponemos el texto de la pregunta

        # Creamos los botones de opción (radio)
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])

        # Guardamos la elección en nuestra lista usando append ()
        respuestas_usuario.append(eleccion)
        st.write("---") # Una línea para separar preguntas

    # Botón obligatorio para cerrar el formulario
    boton_enviar = st.form_submit_button("Entregar Examen")

# 3. LA CORRECCIÓN (Solo ocurre cuando pulsamos el botón)
if boton_enviar:
    aciertos = 0
    # Total es número de preguntas (usa el método len)
    total = len(preguntas)

    # Comparamos las respuestas del usuario con las 'correctas' del archivador
    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos = aciertos + 1
        else:
            aciertos = aciertos -0.25
    if aciertos < 0:
        aciertos = 0

    # Calculamos la nota sobre 10
    nota = (aciertos / total) * 10
    nota_redonda = round(nota, 2)
    print(nota_redonda)
    # Mostramos el resultado con colores
    st.divider()
    st.header(f"Resultado final: {nota_redonda} / 10")
    if nota_redonda < 3:
       st.error("Muy muy mal tio estudia mas")
    elif 3 <= nota_redonda < 5:
       st.warning("Insuficiente pero cerca")
    elif 5 <= nota_redonda < 6:
       st.warning("Ok aprobado tio")
    elif 6 <= nota_redonda < 7:
       st.warning("Buen trabajo sigue asi")
    elif 7 <= nota_redonda < 9:
       st.warning("Notable! que bien")
    elif 9 <= nota_redonda < 10:
       st.warning("Sobresaliente siii")
    elif nota_redonda == 10:
       st.warning("Nota perfecta, Excelente")
