import streamlit as st
import hydralit_components as hc
import base64
from streamlit_elements import elements, mui, html
import streamlit_wordcloud as wordcloud
import streamlit.components.v1 as components
from streamlit_calendar import calendar
import streamlit_antd_components as sac
#Autor: Sergio Lopez

#--------------------------------------------- page config -------------------------------------------------
#basic page configuration
st.set_page_config(
    page_title='CAPA',
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': """# Web Site Club de Algoritmia Avanzada en Python.
                        Todos los derechos reservados 2023, CAPA."""
    }
)

#Disable sidebar
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }

.appview-container .main .block-container{{
    padding-top: 0rem;
    padding-right: 0rem;
    padding-left: 0rem;
    padding-bottom: 0rem;
        }}

</style>
""",
    unsafe_allow_html=True,
)

#--------------------------------------------- Session States -------------------------------------------------------


#If the user is not logged in we create the session state for login state with None
if 'loginst' not in  st.session_state:
    st.session_state.loginst = None

if st.session_state.loginst is not None:
    print('Hello')


#--------------------------------------------- Header -------------------------------------------------------



def pythonlogo(width=25,height=25):
    """
    The `pythonlogo` function displays the Python logo using SVG code and a CSS file.
    """
    with open('src/Frontend/stylepythonlogo.css') as f:
        container1 = st.empty()
        columns1,col2,col3 = st.columns(3)
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        with columns1:
            container1.markdown(
    f'''<svg width="{width}%" height="{height}%" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" id="python-logo">
    <path d="m116 296c0-30.328125 24.671875-55 55-55h170c13.785156 0 25-11.214844 25-25v-141c0-41.355469-33.644531-75-75-75h-70c-41.355469 0-75 33.644531-75 75v41h110c8.285156 0 15 6.714844 15 15s-6.714844 15-15 15h-181c-41.355469 0-75 33.644531-75 75v70c0 41.355469 33.644531 75 75 75h41zm105-220c-8.285156 0-15-6.714844-15-15s6.714844-15 15-15 15 6.714844 15 15-6.714844 15-15 15zm0 0" />
    <path d="m437 146h-41v70c0 30.328125-24.671875 55-55 55h-170c-13.785156 0-25 11.214844-25 25v141c0 41.355469 33.644531 75 75 75h70c41.355469 0 75-33.644531 75-75v-41h-110c-8.285156 0-15-6.714844-15-15s6.714844-15 15-15h181c41.355469 0 75-33.644531 75-75v-70c0-41.355469-33.644531-75-75-75zm-146 290c8.285156 0 15 6.714844 15 15s-6.714844 15-15 15-15-6.714844-15-15 6.714844-15 15-15zm0 0" />
    </svg>''',unsafe_allow_html=True
            )



def show_logos():
    """
    The `show_logos` function displays the Python logo and the name of a Python club using SVG code and a CSS file.
    """


    columns1,col2,col3 = st.columns((0.4,0.4,0.2))

    with col2:
        st.image("resources/logos/LogoCAPPA.png")
    with columns1:
        st.image("resources/logos/logoFESA.png",width=300)
    with col3:
        pythonlogo(30,30)


show_logos()


#--------------------------------------------- Navbar -------------------------------------------------------


if st.session_state.loginst == None:
#navbar items for not logged in users

    user = 'Login'
    menu_data = [
    {'icon': "far fa-copy", 'label':"Docs"},
    {'id':'About','icon':"❓",'label':"FAQ"},
    {'id':'contact','icon':"📩",'label':"Contacto"},
    ]
else:
    menu_data = [
    {'icon': "fa-solid fa-radar",'label':"Problemas", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Basicos"},{'id':'subid12','icon': "fa fa-database", 'label':"Intermedios"},{'id':'subid13','icon': "💀", 'label':"Avanzados"},{'id':'subid14','icon': "🔧", 'label':"Editor"}]},
    {'id':'contest','icon': "🏆", 'label':"Concursos"},
    {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
    {'id':'docs','icon': "far fa-copy", 'label':"Docs"},
    {'id':'code','icon': "👨‍💻", 'label':"Editor de Código"},
    {'icon': "fa-solid fa-radar",'label':"Tests", 'submenu':[{'label':"Basicos 1", 'icon': "🐛"},{'icon':'🐍','label':"Intermedios"},{'icon':'🐉','label':"Avanzados",},{'id':'subid144','icon': "🔧", 'label':"Editor" }]},
    {'id':'About','icon':"❓",'label':"FAQ"},
    {'id':'contact','icon':"📩",'label':"Contacto"},
    {'id':'logout','icon': "🚪", 'label':"Logout"},#no tooltip message

    ]

over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#002B7A'}
menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Inicio',
        login_name=user,
        hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
        sticky_nav=False, #at the top or not
        sticky_mode='jumpy', #jumpy or not-jumpy, but sticky or pinned
    )





#--------------------------------------------- body -------------------------------------------------------
with open('src/Frontend/welcome.html')  as wlcome:
    components.html(wlcome.read(),height=200)




programming_concepts = [
    {
        "text": "Variable",
        "definition": "Una variable es un contenedor para almacenar datos en un programa. Puede contener diferentes tipos de datos, como números, cadenas de texto o booleanos.",
        "example": "x = 10",
        "use_case": "Las variables se utilizan para almacenar y manipular datos en un programa.",
        "value": 16000, "color":"#0E2954"
    },
    {
        "text": "Ciclo For",
        "definition": "Un ciclo for es una estructura de control que se utiliza para iterar sobre una secuencia de elementos, como una lista o una cadena de texto.",
        "example": "for elemento in lista:",
        "use_case": "Se usa para recorrer elementos en una secuencia y realizar una acción en cada iteración.",
        "value": 8500, "color":"#1F6E8C"
    },
    {
        "text": "Función",
        "definition": "Una función es un bloque de código reutilizable que realiza una tarea específica. Puede recibir argumentos y devolver un resultado.",
        "example": "def suma(a, b):\n    return a + b",
        "use_case": "Las funciones se utilizan para organizar y reutilizar el código, así como para modularizar programas.",
        "value": 13400, "color":"#2E8A99"
    },{
        "text": "Algoritmo",
        "definition": "Un algoritmo es un conjunto de instrucciones paso a paso diseñadas para resolver un problema o realizar una tarea específica en un programa.",
        "example": "El algoritmo de ordenación de burbuja es un ejemplo común de un algoritmo de clasificación.",
        "use_case": "Se utilizan para resolver problemas y realizar tareas en programación.",
        "value": 8300, "color":"#84A7A1"
    },
    {
        "text": "Condición",
        "definition": "Una condición es una expresión booleana que determina si se ejecuta un bloque de código en función de si es verdadera o falsa.",
        "example": "if edad >= 18:",
        "use_case": "Las condiciones se utilizan para tomar decisiones en un programa y controlar su flujo.",
        "value": 12400, "color":"#461959"
    },
    {
        "text": "Bucle While",
        "definition": "Un bucle while es una estructura de control que se utiliza para repetir un bloque de código mientras una condición sea verdadera.",
        "example": "while contador < 10:",
        "use_case": "Se utiliza para ejecutar código repetidamente hasta que la condición especificada sea falsa.",
        "value": 10300, "color":"#7A316F"
    },
    {
        "text": "Listas",
        "definition": "Una lista es una estructura de datos que almacena una colección ordenada de elementos. Los elementos pueden ser de diferentes tipos.",
        "example": "mi_lista = [1, 2, 3, 'cuatro']",
        "use_case": "Se utilizan para almacenar y manipular conjuntos de datos relacionados.",
        "value": 31, "color":"#CD6688"
    },
    {
        "text": "Diccionarios",
        "definition": "Un diccionario es una estructura de datos que almacena pares clave-valor. Cada clave está asociada a un valor único.",
        "example": "mi_diccionario = {'nombre': 'Juan', 'edad': 30}",
        "use_case": "Se utilizan para representar datos en forma de mapeo clave-valor.",
        "value": 6000, "color":"#AED8CC"
    },
    {
        "text": "Clase",
        "definition": "Una clase es un plano o plantilla para crear objetos en programación orientada a objetos (POO). Define atributos y métodos para los objetos.",
        "example": "class Persona:\n    def __init__(self, nombre, edad):\n        self.nombre = nombre\n        self.edad = edad",
        "use_case": "Se utilizan para modelar objetos y encapsular comportamientos en la POO.",
        "color":"#454545",'value': 4500
    },
    {
        "text": "Recursión",
        "definition": "La recursión es una técnica en la que una función se llama a sí misma para resolver un problema más grande o repetitivo.",
        "example": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
        "use_case": "Se utiliza para abordar problemas que pueden descomponerse en subproblemas similares más pequeños.",
        "value": 5600, "color":"#FF6000"
    },
    {
        "text": "Interfaz de Usuario (UI)",
        "definition": "La interfaz de usuario es la parte de un programa que interactúa con los usuarios. Incluye elementos gráficos como botones y formularios.",
        "example": "Una aplicación de procesamiento de texto tiene una UI que permite a los usuarios escribir y formatear texto.",
        "use_case": "Se utiliza para crear aplicaciones amigables y accesibles para los usuarios.",
        "value": 1402, "color":"#FFA559"
    },
    {
        "text": "Depuración",
        "definition": "La depuración es el proceso de identificar y corregir errores en un programa. Se utiliza para asegurarse de que el programa funcione correctamente.",
        "example": "Los programadores utilizan herramientas de depuración para rastrear y solucionar problemas en el código.",
        "use_case": "Es esencial para garantizar la calidad y la fiabilidad del software.",
        "value": 5603, "color":"#A9907E"
    },
    {
        "text": "API",
        "definition": "Una API es un conjunto de reglas y protocolos que permiten a diferentes aplicaciones comunicarse y compartir datos y funcionalidades.",
        "example": "Las redes sociales suelen proporcionar API que permiten a los desarrolladores acceder a datos y funciones de la plataforma.",
        "use_case": "Se utilizan para integrar servicios y datos de diferentes fuentes en una aplicación.",
        "value": 1523, "color":"#F3DEBA"
    },
    {
        "text": "Excepciones",
        "definition": "Las excepciones son eventos inesperados o errores que pueden ocurrir durante la ejecución de un programa en Python. Se manejan mediante bloques 'try' y 'except' para gestionar errores de manera controlada.",
        "example": "try:\n    resultado = 10 / 0\nexcept ZeroDivisionError as e:\n    print('Error:', e)",
        "use_case": "El manejo de excepciones permite que un programa continúe ejecutándose incluso después de encontrar errores.",
        "value": 2456,
        "color": "#ABC4AA"
    },
    {
        "text": "Módulos",
        "definition": "Los módulos son archivos de Python que contienen definiciones de funciones, clases y variables. Se utilizan para organizar y reutilizar el código en diferentes programas.",
        "example": "import math\n\ncoseno = math.cos(0)",
        "use_case": "Los módulos en Python permiten dividir el código en partes más pequeñas y mantenibles, y se pueden importar en otros programas.",
        "value": 3128,
        "color": "#B4B4B3"
    },
    {
        "text": "Decoradores",
        "definition": "Un decorador es una función que se utiliza para modificar o extender el comportamiento de otra función o método en Python. Se colocan sobre la definición de una función con el símbolo '@'.",
        "example": "@decorador\n def funcion_a_decorar():\n     pass",
        "use_case": "Los decoradores se utilizan para agregar funcionalidades adicionales a funciones o métodos sin modificar su código interno.",
        "value": 1897,
        "color": "#26577C"
    },
    {
        "text": "Comprensiones de Listas",
        "definition": "Las comprensiones de listas son una forma concisa de crear listas en Python mediante una expresión y un bucle 'for'. Son útiles para filtrar y transformar datos de manera eficiente.",
        "example": "cuadrados = [x**2 for x in range(10)]",
        "use_case": "Las comprensiones de listas simplifican la creación de listas a partir de secuencias de datos existentes.",
        "value": 987,
        "color": "#E55604"
    },
    {
        "text": "Herencia",
        "definition": "La herencia es un concepto de la programación orientada a objetos en Python que permite crear nuevas clases basadas en clases existentes. La clase derivada hereda atributos y métodos de la clase base.",
        "example": "class Animal:\n    def hablar(self):\n        pass\n\nclass Perro(Animal):\n    def hablar(self):\n        return 'Woof'",
        "use_case": "La herencia se utiliza para reutilizar y extender comportamientos de clases existentes.",
        "value": 1523,
        "color": "#27005D"
    },
    {
        "text": "Expresiones Regulares",
        "definition": "Las expresiones regulares, o regex, son patrones de búsqueda utilizados para encontrar y manipular texto en Python. El módulo 're' proporciona funciones para trabajar con expresiones regulares.",
        "example": "import re\n\npatron = r'\d+'  # Encuentra uno o más dígitos\nresultado = re.findall(patron, '123 abc 456')",
        "use_case": "Las expresiones regulares se utilizan para realizar búsquedas avanzadas y manipular texto en cadenas de caracteres.",
        "value": 2456,
        "color": "#9400FF"
    },
    {
        "text": "Manejo de Archivos",
        "definition": "Python proporciona funciones y métodos para trabajar con archivos en el sistema de archivos. Se pueden abrir, leer, escribir y cerrar archivos de manera eficiente.",
        "example": "with open('archivo.txt', 'r') as archivo:\n    contenido = archivo.read()",
        "use_case": "El manejo de archivos es esencial para leer y escribir datos en programas Python.",
        "value": 3128,
        "color": "#AED2FF"
    },
    {
        "text": "Virtualenv",
        "definition": "Virtualenv es una herramienta que permite crear entornos virtuales aislados en Python. Cada entorno virtual puede tener sus propias bibliotecas y versiones de Python, lo que facilita la gestión de dependencias y proyectos.",
        "example": "virtualenv mi_entorno\nsource mi_entorno/bin/activate",
        "use_case": "Virtualenv se utiliza para evitar conflictos de dependencias y mantener proyectos Python independientes.",
        "value": 1897,
        "color": "#191D88"
    },
    {
        "text": "Pip",
        "definition": "Pip es el administrador de paquetes de Python, utilizado para instalar, actualizar y administrar bibliotecas y paquetes de Python desde el repositorio de PyPI (Python Package Index).",
        "example": "pip install nombre_del_paquete",
        "use_case": "Pip es esencial para gestionar las dependencias de un proyecto Python.",
        "value": 987,
        "color": "#1450A3"
    },
    {
        "text": "Iteradores",
        "definition": "Los iteradores en Python son objetos que permiten recorrer una secuencia de elementos uno por uno. Se implementan mediante los métodos `__iter__()` y `__next__()` en una clase.",
        "example": "Puedes crear tus propios iteradores o utilizar los iteradores incorporados en Python, como `range()` y `enumerate()`.",
        "use_case": "Se utilizan para recorrer colecciones de datos, como listas, diccionarios y conjuntos, de manera eficiente y controlada.",
        "value": 1011,
        "color": "#3498db"
    },
    {
        "text": "Comprensión de Conjuntos y Diccionarios",
        "definition": "Además de la comprensión de listas, Python también admite la comprensión de conjuntos y diccionarios. Estas expresiones permiten crear conjuntos y diccionarios de manera concisa.",
        "example": "Ejemplo de comprensión de conjunto: `{x**2 for x in range(10)}` crea un conjunto de los cuadrados de los números del 0 al 9.",
        "use_case": "Se utilizan para crear conjuntos y diccionarios de manera eficiente y expresiva a partir de iterables o secuencias.",
        "value": 1112,
        "color": "#e74c3c"
    },
    {
        "text": "Módulo 'requests'",
        "definition": "El módulo 'requests' es una biblioteca de Python ampliamente utilizada para realizar solicitudes HTTP a servidores web. Facilita la realización de peticiones GET, POST y otras operaciones relacionadas con HTTP.",
        "example": "Puedes usar el módulo 'requests' para interactuar con APIs web y acceder a recursos en línea desde tu programa Python.",
        "use_case": "Se utiliza para realizar solicitudes y recibir respuestas HTTP, lo que es esencial para la integración de servicios web en aplicaciones.",
        "value": 1213,
        "color": "#9b59b6"
    },
    {
        "text": "Generadores",
        "definition": "Los generadores en Python son funciones que generan valores de manera perezosa (on-demand) en lugar de generar una lista completa de valores. Esto ahorra memoria y es eficiente en términos de rendimiento.",
        "example": "Puedes crear generadores utilizando la sintaxis de función y la declaración `yield` en lugar de `return`.",
        "use_case": "Se utilizan cuando necesitas generar secuencias de valores de manera eficiente sin cargar toda la secuencia en memoria.",
        "value": 1415,
        "color": "#27ae60"
    },
    {
        "text": "NumPy",
        "definition": "NumPy es una biblioteca de Python ampliamente utilizada para realizar operaciones matemáticas y numéricas en matrices y arreglos multidimensionales. Proporciona estructuras de datos eficientes y funciones de alto rendimiento.",
        "example": "Puedes usar NumPy para realizar cálculos matriciales, estadísticas, procesamiento de señales y mucho más.",
        "use_case": "Se utiliza en aplicaciones científicas, de ingeniería y de análisis de datos donde se requiere manipulación eficiente de datos numéricos.",
        "value": 1516,
        "color": "#e67e22"
    },
    {
        "text": "Django",
        "definition": "Django es un framework de desarrollo web de alto nivel y de código abierto en Python. Proporciona una estructura sólida para construir aplicaciones web, con una amplia gama de características incorporadas.",
        "example": "Django se utiliza en la creación de aplicaciones web de todos los tamaños, desde pequeñas aplicaciones hasta sitios web de gran envergadura.",
        "use_case": "Se utiliza para el desarrollo rápido y eficiente de aplicaciones web, ya que incluye manejo de bases de datos, autenticación de usuarios, enrutamiento y más.",
        "value": 1617,
        "color": "#3498db"
    },
    {
        "text": "PyCharm",
        "definition": "PyCharm es un popular IDE desarrollado por JetBrains para programar en Python. Ofrece un conjunto de herramientas poderosas para el desarrollo, depuración y análisis de código Python.",
        "example": "PyCharm proporciona características como resaltado de sintaxis, depuración interactiva, autocompletado y gestión de proyectos.",
        "use_case": "Se utiliza como un entorno de desarrollo eficiente para proyectos de Python, desde pequeños scripts hasta aplicaciones complejas.",
        "value": 1718,
        "color": "#9b59b6"
    },
    {
        "text": "Flask",
        "definition": "Flask es un microframework de Python para el desarrollo web. Es minimalista y ofrece las herramientas esenciales para crear aplicaciones web, permitiendo una gran flexibilidad en la elección de componentes adicionales.",
        "example": "Flask se utiliza para crear aplicaciones web ligeras y rápidas, como sitios web pequeños, servicios web API y aplicaciones web de una sola página (SPA).",
        "use_case": "Se utiliza cuando se necesita desarrollar aplicaciones web de manera rápida y sencilla sin una sobrecarga de características.",
        "value": 1920,
        "color": "#27ae60"
    },
    {
        "text": "Tkinter",
        "definition": "Tkinter es un módulo estándar de Python que permite crear interfaces gráficas de usuario (GUI). Proporciona herramientas para crear ventanas, botones, cuadros de texto y otros elementos de GUI.",
        "example": "Tkinter se utiliza para desarrollar aplicaciones de escritorio con una interfaz de usuario interactiva.",
        "use_case": "Se utiliza cuando necesitas crear aplicaciones de escritorio con una interfaz de usuario amigable y componentes interactivos.",
        "value": 2122,
        "color": "#3498db"
    },

    {
        "text": "Matplotlib",
        "definition": "Matplotlib es una biblioteca de Python ampliamente utilizada para crear gráficos y visualizaciones de datos de alta calidad. Ofrece una gran flexibilidad en la creación de gráficos personalizados.",
        "example": "Puedes utilizar Matplotlib para crear gráficos de barras, gráficos de dispersión, gráficos de líneas y mucho más, y personalizar su apariencia según tus necesidades.",
        "use_case": "Se utiliza en la ciencia de datos, análisis de datos, informes y presentaciones para visualizar datos de manera efectiva.",
        "value": 2223,
        "color": "#9b59b6"
    },
    {
        "text": "conda",
        "definition": "Conda es una herramienta de gestión de entornos y paquetes que facilita la creación, activación y gestión de entornos virtuales para proyectos de Python. Además, permite la instalación y administración de paquetes de manera eficiente.",
        "example": "Conda se utiliza para crear entornos virtuales independientes para proyectos de Python y gestionar las dependencias de manera efectiva.",
        "use_case": "Se utiliza para mantener proyectos Python aislados con sus propias dependencias y versiones de paquetes.",
        "value": 2324,
        "color": "#e74c3c"
    },
    {
        "text": "asyncio",
        "definition": "Asyncio es un módulo incorporado en Python que permite la programación asincrónica. Facilita la escritura de código que puede realizar múltiples tareas de manera eficiente sin bloquear el hilo principal.",
        "example": "Puedes utilizar 'asyncio' para escribir servidores web, aplicaciones de red y tareas de E/S de manera asincrónica.",
        "use_case": "Se utiliza cuando se necesita gestionar muchas tareas simultáneas de manera eficiente, como en aplicaciones web y servicios de red.",
        "value": 2526,
        "color": "#d35400"
    }
    # Continúa agregando más textos en el mismo formato.
]


ml_data_science_concepts = [
    {
        "text": "Machine Learning",
        "definition": "El Aprendizaje Automático es un subcampo de la inteligencia artificial que se enfoca en desarrollar algoritmos y modelos que permiten a las máquinas aprender de datos y realizar tareas sin ser programadas explícitamente.",
        "example": "Entrenar un modelo de Machine Learning para predecir el precio de las viviendas basado en datos históricos.",
        "use_case": "El Machine Learning se utiliza en una variedad de aplicaciones, incluyendo clasificación de texto, recomendaciones personalizadas y reconocimiento de patrones.",
        "value": 1523,
        "color": "#191D88"
    },
    {
        "text": "Regresión",
        "definition": "La regresión es una técnica de Machine Learning que se utiliza para predecir valores numéricos basados en datos históricos. Puede ser lineal o no lineal, dependiendo de la relación entre las variables de entrada y la variable objetivo.",
        "example": "La regresión lineal se utiliza para predecir el precio de una casa en función de características como el número de habitaciones y el área.",
        "use_case": "La regresión se utiliza en problemas de predicción numérica, como predicción de precios, demanda de productos, etc.",
        "value": 2456,
        "color": "#1450A3"
    },
    {
        "text": "Clasificación",
        "definition": "La clasificación es una técnica de Machine Learning que se utiliza para predecir una etiqueta o categoría a partir de un conjunto de características. Se utiliza en problemas donde la variable objetivo es categórica.",
        "example": "Clasificar correos electrónicos como spam o no spam en función de su contenido y características.",
        "use_case": "La clasificación se aplica en detección de fraudes, diagnóstico médico, reconocimiento de imágenes y más.",
        "value": 3128,
        "color": "#337CCF"
    },
    {
        "text": "Redes Neuronales",
        "definition": "Las redes neuronales artificiales son un modelo de Machine Learning inspirado en el funcionamiento del cerebro humano. Consisten en capas de neuronas interconectadas que se utilizan para realizar tareas de aprendizaje profundo.",
        "example": "Una red neuronal convolucional (CNN) se utiliza para el reconocimiento de imágenes en aplicaciones como reconocimiento de objetos y detección de rostros.",
        "use_case": "Las redes neuronales se aplican en tareas de procesamiento de imágenes, procesamiento de lenguaje natural (NLP) y juegos.",
        "value": 1897,
        "color": "#FFC436"
    },
    {
        "text": "Aprendizaje Supervisado",
        "definition": "El aprendizaje supervisado es un tipo de Machine Learning donde el modelo se entrena utilizando datos etiquetados, es decir, datos con pares de entrada y salida conocidos. El aprendizaje no supervisado implica el entrenamiento sin etiquetas, lo que permite al modelo encontrar patrones por sí mismo.",
        "example": "Clasificación de spam es un ejemplo de aprendizaje supervisado, mientras que la segmentación de clientes en grupos sin etiquetas es un ejemplo de aprendizaje no supervisado.",
        "use_case": "El aprendizaje supervisado se utiliza en problemas de predicción y clasificación, mientras que el no supervisado se utiliza en la segmentación y reducción de dimensiones.",
        "value": 987,
        "color": "#7A9D54"
    },
    {
        "text": "Validación Cruzada",
        "definition": "La validación cruzada es una técnica para evaluar el rendimiento de un modelo de Machine Learning utilizando datos de entrenamiento y prueba de manera repetida. Ayuda a estimar cómo se comportará el modelo con datos no vistos.",
        "example": "La validación cruzada k-fold divide los datos en k partes iguales, entrena y evalúa el modelo k veces, utilizando cada parte como conjunto de prueba en una iteración diferente.",
        "use_case": "La validación cruzada es esencial para evitar el sobreajuste y seleccionar modelos que generalicen bien.",
        "value": 2456,
        "color": "#557A46"
    },
    {
        "text": "NLP",
        "definition": "El Procesamiento de Lenguaje Natural es una rama de la inteligencia artificial que se enfoca en la interacción entre las computadoras y el lenguaje humano. Se utiliza para analizar, comprender y generar texto en lenguaje natural.",
        "example": "El análisis de sentimientos en redes sociales, donde se identifican opiniones positivas o negativas en comentarios de usuarios.",
        "use_case": "El NLP se aplica en chatbots, traducción automática, resumen de texto, y análisis de texto para insights empresariales.",
        "value": 10000,
        "color": "#8C3333"
    },
    {
        "text": "Deep Learning",
        "definition": "El Aprendizaje Profundo es una subárea del Machine Learning que utiliza redes neuronales profundas con múltiples capas ocultas para resolver problemas complejos. Se ha destacado en tareas de visión por computadora, procesamiento de lenguaje natural y más.",
        "example": "Las redes neuronales convolucionales (CNN) se utilizan en Aprendizaje Profundo para reconocimiento de imágenes.",
        "use_case": "El Aprendizaje Profundo se aplica en reconocimiento de voz, detección de objetos, conducción autónoma y más.",
        "value": 1523,
        "color": "#37306B"
    },
    {
        "text": "Árboles de Decisión",
        "definition": "Un Árbol de Decisión es una técnica de Machine Learning utilizada para la toma de decisiones basada en condiciones lógicas. Divide un conjunto de datos en subconjuntos más pequeños y, finalmente, toma decisiones basadas en reglas.",
        "example": "Un Árbol de Decisión para clasificar si un correo electrónico es spam o no spam basado en características como palabras clave y remitente.",
        "use_case": "Los Árboles de Decisión se aplican en clasificación, regresión y toma de decisiones automatizadas.",
        "value": 2456,
        "color": "#66347F"
    },
    {
        "text": "TensorFlow",
        "definition": "TensorFlow es una biblioteca de código abierto desarrollada por Google para Machine Learning y Aprendizaje Profundo. Se utiliza para construir y entrenar modelos de redes neuronales de manera eficiente.",
        "example": "Entrenamiento de una red neuronal en TensorFlow para tareas de visión por computadora.",
        "use_case": "TensorFlow se utiliza en una amplia gama de aplicaciones de Aprendizaje Profundo, desde reconocimiento de voz hasta procesamiento de imágenes.",
        "value": 3128,
        "color": "#9E4784"
    },
    {
        "text": "Pandas",
        "definition": "Pandas es una biblioteca de Python ampliamente utilizada para la manipulación y análisis de datos. Proporciona estructuras de datos flexibles y herramientas para limpiar, transformar y analizar datos de manera eficiente.",
        "example": "Carga y manipulación de datos en un DataFrame de Pandas para su análisis.",
        "use_case": "Pandas es esencial en Ciencia de Datos para explorar y preparar datos antes de aplicar técnicas de Machine Learning.",
        "value": 1897,
        "color": "#D27685"
    },
    {
        "text": "SciKit-Learn",
        "definition": "SciKit-Learn es una biblioteca de Python que proporciona herramientas para Machine Learning y Ciencia de Datos. Incluye algoritmos de clasificación, regresión, agrupamiento y más, junto con utilidades para la evaluación de modelos.",
        "example": "Entrenamiento de un modelo de clasificación en SciKit-Learn y evaluación de su rendimiento.",
        "use_case": "SciKit-Learn es ampliamente utilizado en proyectos de Machine Learning para implementar algoritmos y evaluar modelos.",
        "value": 987,
        "color": "#9A3B3B"
    },
    {
        "text": "RNN",
        "definition": "Las Redes Neuronales Recurrentes son un tipo de red neuronal que se utiliza en secuencias de datos, como texto o series temporales. Pueden recordar estados anteriores y son útiles para tareas como traducción automática y análisis de texto.",
        "example": "Traducción automática de un idioma a otro utilizando una RNN.",
        "use_case": "Las RNN se aplican en tareas de procesamiento de lenguaje natural, reconocimiento de voz y predicción de series temporales.",
        "value": 2456,
        "color": "#C08261"
    },
    {
        "text": "Clustering",
        "definition": "El clustering es una técnica de aprendizaje no supervisado que se utiliza para dividir un conjunto de datos en grupos o clusters basados en similitudes entre los puntos de datos. Los puntos dentro del mismo grupo son más similares entre sí que con los de otros grupos.",
        "example": "Agrupamiento de clientes en segmentos con características similares para campañas de marketing personalizadas.",
        "use_case": "El clustering se aplica en segmentación de clientes, análisis de redes sociales y más.",
        "value": 3128,
        "color": "#0F2C59"
    },
]


advanced_concepts = [
    {
        "text": "Búsqueda Binaria",
        "definition": "La Búsqueda Binaria es un algoritmo eficiente para encontrar un elemento en una lista ordenada. Divide repetidamente la lista a la mitad y compara el valor deseado con el valor en el medio hasta encontrar la coincidencia.",
        "example": "La Búsqueda Binaria se utiliza comúnmente en la búsqueda de elementos en listas ordenadas, como directorios telefónicos o bases de datos indexadas.",
        "use_case": "Cuando tienes una gran cantidad de datos ordenados y necesitas buscar rápidamente un elemento específico, la Búsqueda Binaria es una elección eficiente.",
        "value": 1234,
        "color": "#ff5733"
    },
    {
        "text": "Programación Dinámica",
        "definition": "La Programación Dinámica es una técnica para resolver problemas dividiéndolos en subproblemas más pequeños y resolviendo cada subproblema una sola vez, almacenando las soluciones para su reutilización.",
        "example": "La Programación Dinámica se usa en problemas como el cálculo del número de formas de llegar a un punto en un gráfico o encontrar la secuencia de operaciones óptima para una cadena de matrices.",
        "use_case": "Cuando un problema puede descomponerse en subproblemas que se solucionan de manera independiente y se pueden reutilizar, la Programación Dinámica puede mejorar significativamente el rendimiento.",
        "value": 2345,
        "color": "#3498db"
    },
    {
        "text": "Algoritmo Genético",
        "definition": "Los Algoritmos Genéticos son una técnica de optimización inspirada en la evolución biológica. Utilizan una población de soluciones candidatas, aplican operadores genéticos y evolucionan a través de generaciones para encontrar la mejor solución posible.",
        "example": "Los Algoritmos Genéticos se aplican en problemas de optimización, como la planificación de rutas, el diseño de circuitos electrónicos y la optimización de parámetros en aprendizaje automático.",
        "use_case": "Cuando necesitas encontrar soluciones óptimas en un espacio de búsqueda complejo y amplio, los Algoritmos Genéticos pueden ser una opción poderosa.",
        "value": 3456,
        "color": "#e74c3c"
    },
    {
        "text": "Kruskal",
        "definition": "El Algoritmo de Kruskal es un algoritmo de grafos que encuentra el árbol de expansión mínima en un grafo ponderado, conectando todos los vértices con el costo total más bajo posible.",
        "example": "Se utiliza en problemas de diseño de redes, como la planificación de rutas de cableado o la optimización de redes de comunicación.",
        "use_case": "Cuando necesitas conectar un conjunto de ubicaciones de manera eficiente, minimizando el costo total de la conexión, el Algoritmo de Kruskal es una opción valiosa.",
        "value": 4567,
        "color": "#1abc9c"
    },
    {
        "text": "Floyd-Warshall",
        "definition": "El Algoritmo de Floyd-Warshall es un algoritmo para encontrar los caminos más cortos entre todos los pares de vértices en un grafo ponderado, incluso si hay arcos de peso negativo.",
        "example": "Se utiliza en problemas de planificación de rutas, optimización de redes y análisis de grafos para encontrar la distancia más corta entre todos los pares de ubicaciones.",
        "use_case": "Cuando necesitas encontrar las distancias más cortas entre todos los pares de nodos en un grafo, el Algoritmo de Floyd-Warshall es una opción eficaz.",
        "value": 5678,
        "color": "#9b59b6"
    },
    {
        "text": "Dijkstra",
        "definition": "El Algoritmo de Dijkstra es un algoritmo de búsqueda de caminos más cortos en un grafo ponderado dirigido o no dirigido. Encuentra el camino más corto desde un nodo de inicio a todos los demás nodos en el grafo.",
        "example": "Se utiliza en problemas de navegación, planificación de rutas y redes de transporte para encontrar las rutas más cortas desde un origen a múltiples destinos.",
        "use_case": "Cuando necesitas encontrar el camino más corto desde un punto de partida a varios destinos en un grafo ponderado, el Algoritmo de Dijkstra es una elección común.",
        "value": 6789,
        "color": "#f39c12"
    },
    {
        "text": "Backtracking",
        "definition": "El Backtracking es una técnica de resolución de problemas que se basa en explorar todas las posibles soluciones de manera recursiva, retrocediendo (backtracking) cuando se llega a una solución inválida o insatisfactoria.",
        "example": "Se utiliza en problemas de búsqueda exhaustiva, como el Sudoku, el problema de las N reinas y la resolución de laberintos.",
        "use_case": "Cuando necesitas encontrar todas las soluciones posibles para un problema, incluso si implica explorar un gran espacio de búsqueda, el Backtracking es útil.",
        "value": 7890,
        "color": "#27ae60"
    },
    {
        "text": "Programación Funcional",
        "definition": "La Programación Funcional es un estilo de programación que se basa en el uso de funciones puras y la inmutabilidad de los datos. Python admite características de programación funcional, como funciones de orden superior y lambda.",
        "example": "Puedes utilizar funciones como `map()`, `filter()`, y `reduce()` para realizar operaciones en listas de manera funcional.",
        "use_case": "Se utiliza cuando deseas escribir código más declarativo y conciso, y cuando trabajas con operaciones de transformación de datos.",
        "value": 9012,
        "color": "#27ae60"
    }
]



# Puedes seguir añadiendo más conceptos relacionados con Machine Learning y Ciencia de Datos según tus necesidades.





return_obj = wordcloud.visualize(programming_concepts+ml_data_science_concepts+advanced_concepts, tooltip_data_fields={
        'text':'Concepto', 'definition':'Definición', 'example':'Ejemplo',
        'use_case': 'Uso'
        }, per_word_coloring=True,layout='archimedean',padding=3,font_min=18, font_max=72)

st.divider()

with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    from streamlit_elements import dashboard

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 6, 3, isDraggable=True),
        dashboard.Item("second_item", 0, 4, 6, 3, isDraggable=True, moved=False),
        dashboard.Item("third_item", 6, 0, 6, 3, isResizable=True),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

    with dashboard.Grid(layout):
        from streamlit_elements import media

        media.Player(url="https://www.youtube.com/watch?v=iik25wqIuFo", controls=True,key="first_item")
        with mui.Card(key="second_item", sx={"display": "flex", "flexDirection": "column", "borderRadius": 2, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="¿ Por qué usar Streamlit 🍅 ?",
                subheader="Septiembre 21, 2023",
                avatar=mui.Avatar("U", sx={"bgcolor": "blue"}),
                action=mui.IconButton(mui.icon.MoreVert),

            )
            mui.CardMedia(
                component="img",
                height=194,
                image="https://cdn.analyticsvidhya.com/wp-content/uploads/2021/10/64750featred.jpg",
                alt="streamlit logo",
            )

            with mui.CardContent(sx={"flex": 1}):
                mui.Typography('Streamlit es una biblioteca de Python que simplifica drásticamente la creación de aplicaciones web interactivas. Su mayor ventaja radica en la facilidad de uso, ya que permite a los desarrolladores crear aplicaciones web funcionales utilizando solo Python.')

            with mui.CardActions(disableSpacing=True):
                mui.IconButton(mui.icon.Favorite)
                mui.IconButton(mui.icon.Share)
        #dashboard.card("Second item (cannot drag)",key="second_item")
        #mui.Paper("Third item (cannot resize)", key="third_item")

        with mui.Card(key="third_item", sx={"display": "flex", "flexDirection": "column", "borderRadius": 2, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="¿ Por qué aprender Python ?",
                subheader="Septiembre 22, 2023",
                avatar=mui.Avatar("S", sx={"bgcolor": "green"}),
                action=mui.IconButton(mui.icon.MoreVert),

            )
            mui.CardMedia(
                component="img",
                height=194,
                image="data:image/jpeg;base64,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",
                alt="python logo",
            )

            with mui.CardContent(sx={"flex": 1}):
                mui.Typography('Aprender Python es una elección inteligente porque es un lenguaje de programación versátil y fácil de aprender. Python se utiliza ampliamente en una variedad de campos, desde desarrollo web y científico hasta automatización y aprendizaje automático. Además, su sintaxis legible y su gran comunidad de desarrolladores hacen que sea una excelente opción para principiantes y profesionales por igual.')

            with mui.CardActions(disableSpacing=True):
                mui.IconButton(mui.icon.Favorite)
                mui.IconButton(mui.icon.Share)


st.header('Calendario')

mode = st.selectbox(
        "Calendar Mode:",
        (
            "daygrid",
            "timegrid",
            "timeline",
            "resource-daygrid",
            "resource-timegrid",
            "resource-timeline",
            "list",
            "multimonth",
        ),
    )

events = [
        {
            "title": "Event 1",
            "color": "#FF6C6C",
            "start": "2023-11-03",
            "end": "2023-11-05",
            "resourceId": "a",
        },
        {
            "title": "Event 2",
            "color": "#FFBD45",
            "start": "2023-10-01",
            "end": "2023-10-10",
            "resourceId": "b",
        },
        {
            "title": "Event 3",
            "color": "#FF4B4B",
            "start": "2023-09-20",
            "end": "2023-09-20",
            "resourceId": "c",
        },
        {
            "title": "Event 4",
            "color": "#FF6C6C",
            "start": "2023-09-20",
            "end": "2023-09-20",
            "resourceId": "d",
        },
        {
            "title": "Event 5",
            "color": "#FFBD45",
            "start": "2023-09-20",
            "end": "2023-09-22",
            "resourceId": "e",
        },
        {
            "title": "Event 6",
            "color": "#FF4B4B",
            "start": "2023-07-28",
            "end": "2023-07-20",
            "resourceId": "f",
        },
        {
            "title": "Event 7",
            "color": "#FF4B4B",
            "start": "2023-07-01T08:30:00",
            "end": "2023-07-01T10:30:00",
            "resourceId": "a",
        },
        {
            "title": "Event 8",
            "color": "#3D9DF3",
            "start": "2023-07-01T07:30:00",
            "end": "2023-07-01T10:30:00",
            "resourceId": "b",
        },
        {
            "title": "Event 9",
            "color": "#3DD56D",
            "start": "2023-07-02T10:40:00",
            "end": "2023-07-02T12:30:00",
            "resourceId": "c",
        },
        {
            "title": "Event 10",
            "color": "#FF4B4B",
            "start": "2023-07-15T08:30:00",
            "end": "2023-07-15T10:30:00",
            "resourceId": "d",
        },
        {
            "title": "Event 11",
            "color": "#3DD56D",
            "start": "2023-07-15T07:30:00",
            "end": "2023-07-15T10:30:00",
            "resourceId": "e",
        },
        {
            "title": "Event 12",
            "color": "#3D9DF3",
            "start": "2023-07-21T10:40:00",
            "end": "2023-07-21T12:30:00",
            "resourceId": "f",
        },
        {
            "title": "Event 13",
            "color": "#FF4B4B",
            "start": "2023-07-17T08:30:00",
            "end": "2023-07-17T10:30:00",
            "resourceId": "a",
        },
        {
            "title": "Event 14",
            "color": "#3D9DF3",
            "start": "2023-07-17T09:30:00",
            "end": "2023-07-17T11:30:00",
            "resourceId": "b",
        },
        {
            "title": "Event 15",
            "color": "#3DD56D",
            "start": "2023-07-17T10:30:00",
            "end": "2023-07-17T12:30:00",
            "resourceId": "c",
        },
        {
            "title": "Event 16",
            "color": "#FF6C6C",
            "start": "2023-07-17T13:30:00",
            "end": "2023-07-17T14:30:00",
            "resourceId": "d",
        },
        {
            "title": "Event 17",
            "color": "#FFBD45",
            "start": "2023-07-17T15:30:00",
            "end": "2023-07-17T16:30:00",
            "resourceId": "e",
        },
    ]
calendar_resources = [
        {"id": "a", "building": "Building A", "title": "Room A"},
        {"id": "b", "building": "Building A", "title": "Room B"},
        {"id": "c", "building": "Building B", "title": "Room C"},
        {"id": "d", "building": "Building B", "title": "Room D"},
        {"id": "e", "building": "Building C", "title": "Room E"},
        {"id": "f", "building": "Building C", "title": "Room F"},
    ]

calendar_options = {
        "editable": "true",
        "navLinks": "true",
        "resources": calendar_resources,
    }

if "resource" in mode:
    if mode == "resource-daygrid":
        calendar_options = {
                **calendar_options,
                "initialDate": "2023-07-01",
                "initialView": "resourceDayGridDay",
                "resourceGroupField": "building",
            }
    elif mode == "resource-timeline":
        calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
                },
                "initialDate": "2023-07-01",
                "initialView": "resourceTimelineDay",
                "resourceGroupField": "building",
            }
    elif mode == "resource-timegrid":
            calendar_options = {
                **calendar_options,
                "initialDate": "2023-07-01",
                "initialView": "resourceTimeGridDay",
                "resourceGroupField": "building",
            }
    else:
        if mode == "daygrid":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "dayGridDay,dayGridWeek,dayGridMonth",
                },
                "initialDate": "2023-07-01",
                "initialView": "dayGridMonth",
            }
        elif mode == "timegrid":
            calendar_options = {
                **calendar_options,
                "initialView": "timeGridWeek",
            }
        elif mode == "timeline":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "timelineDay,timelineWeek,timelineMonth",
                },
                "initialDate": "2023-07-01",
                "initialView": "timelineMonth",
            }
        elif mode == "list":
            calendar_options = {
                **calendar_options,
                "initialDate": "2023-07-01",
                "initialView": "listMonth",
            }
        elif mode == "multimonth":
            calendar_options = {
                **calendar_options,
                "initialView": "multiMonthYear",
            }

state = calendar(
        events=events,
        options=calendar_options,
        key=mode,
    )
#st.write(state)

st.markdown('''
<div style="text-align: center;">
<h1 style="font-size: 30px;font-weight: bold;font-family: 'Courier New'">Redes Sociales</h1>
</div>
''',unsafe_allow_html=True)
sac.segmented(

    items=[

        sac.SegmentedItem(label='facebook',icon='facebook' ),

        sac.SegmentedItem(label='Instagram', icon='instagram' ),

    ], format_func='title', radius='lg', size='lg', align='center', grow=False

)


#------------------------------------- Footer ---------------------------------------------------------
st.divider()
with open('src/Frontend/footer.html') as foo:
    #components.html(foo.read(),width=1600)
    st.markdown(foo.read(), unsafe_allow_html=True)
