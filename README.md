<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# **Link de la aplicacion de consulta y recomendacion de peliculas:** **[API deploy](https://api-pi-danser.onrender.com/docs#/)** :sunglasses:

<h1 align=center> Proyecto Individual #1 Data Science - MLOps </h1>

<h2 align=center> En que consiste el proyecto :point_right:</h2>

A partir de 2 bases de datos no estructuradas de peliculas, se realizo el proceso ETL, se realizo un modelo de ML basado en contenido  para la recomendación de peliculas y se dispuso de todo este tratamiento en una API para se sea consumida por cualquier departamento de la compañia.

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

<h1 align=center>Desarrollo del trabajo :construction_worker:</h1>

# - **Extracción, transformacion y carga - ETL**

Cuento con 2 archivos csv.

* movies: que es donde esta toda la informacion de la pelicula como, titulo, overview, gasto, ingresos, tiempo de duracion, genero, compañia que la desarrollo, paises donde fue grabada, idiomas a las que fue traducido, etc.
    
* credits: que cuenta con la informacion de todos los empleados que conformaron la pelicula yendo desde el directores y actores hasta productos musicales.

Mis datos cuentan con poca madurez(ok, es nula 😭): Datos anidados, sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas, haciendo mi trabajo imposible 😩.

Se empezo desde cero, haciendo un trabajo de Data Engineer 🤯, se inicia con el proceso ETL, consistiendo este en desanidar la informacion que esta contenida dentro de los diccionarios en algunos de los campos del dataset, se modelo a una base de datos relacional.

Los dataset originales se encuentran alojados en [Datasets](https://github.com/danser996/PI_DS/tree/master/Dataset).

Todo el proceso ETL se encuentra en [proceso ETL](https://github.com/danser996/PI_DS/tree/master/code).

<p align=center><img src=https://tableauperu.com/wp-content/uploads/2021/10/que-es-etl-1024x1024.png><p>

## - **Sistema de recomendacion de peliculas** :wink:
## Tratamiento de campos usados para el modelo ML

Para el sistema de recomendacion de peliculas tome del dataset limpio los campos title(titulo de la pelicula), name_actor(nombre de los actores de la pelicula) y overview(descripcion general de la pelicula), tome todos los actores de cada pelicula y los uni a una lista, cada pelicula contaba con los campos titulo, overview y lista de actores que la conforman,las lista de actores se unieron para que quedaron todos en un solo string asi: 
```python
actors = ['Jim Varney', 'John Ratzenberger', 'Wallace Shawn']
' '.join(actors)
'Jim Varney John Ratzenberger Wallace Shawn'
```
Finalmente se concateno los campos title, overview y name_actor y se guardo en un nuevo campo (tags), cada pelicula cuenta con un campo llamado tags, en él esta escrito el nombre de la pelicula, el overview y los actores que en ella trabajan quedando por ejemplo de la siguiente manera:

```python
campo_concat 
"toy story tom hanks tim allen don rickles jim varney wallace shawn john ratzenberger annie potts john morris erik von detten laurie metcalf r. lee ermey sarah freeman penn jillette animation comedy family led by woody, andy's toys live happily in his room until andy's birthday brings buzz lightyear onto the scene. afraid of losing his place in andy's heart, woody plots against buzz. but when circumstances separate buzz and woody from their owner, the duo eventually learns to put aside their differences."
```

## **Modelo machine learning**

## NLP (Natural Language Processing)

Es un campo de estudio dentro de la inteligencia artificial y la lingüística computacional que se centra en la interacción entre las computadoras y el lenguaje humano. El objetivo principal del NLP es permitir que las máquinas comprendan, interpreten y generen el lenguaje humano de manera natural.

Preprocesamiento de texto: Aplica técnicas de preprocesamiento de texto para convertir el texto en un formato adecuado para el análisis. Esto puede incluir tokenización (dividir el texto en unidades más pequeñas, como palabras o frases), eliminación de stopwords (palabras comunes sin valor informativo) y normalización de palabras (por ejemplo, convertir palabras en su forma base, como "corriendo" a "correr").

## Algoritmo utilizado: Similaridad del coseno

La similaridadd del coseno es una medida utilizada en el procesamiento del lenguaje natural y en la recuperación de información para determinar la similitud entre dos vectores de características. Se calcula utilizando el coseno del ángulo entre los vectores en un espacio vectorial.

El resultado de la similaridad del coseno es un valor entre -1 y 1. Un valor de 1 indica una similitud perfecta entre los vectores, mientras que un valor de -1 indica una similitud completamente opuesta. Un valor cercano a 0 indica poca similitud entre los vectores.

![Similaridad coseno](/src/SIM_COSINE.png)

## Scikit-Learn
Se utilizo el modulo Scikit-learn y la clase TfidfVectorizer de sklearn para calcular la frecuencia de las palabras que aparecen en el campo tags y se ignoraron todas las palabras comunes del ingles(stopwords) ya que no aportar valor a mi modelamiento.

<!-- ![Sklearn modulo](/src/skl.png) -->
<p align=center><img src=https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg><p>

```python
tfidf = TfidfVectorizer(stop_words='english')
df['tags'].fillna('', inplace=True) # reemplazamos los valores nulos del dataframe por un vacio
tfidf_matrix = tfidf.fit_transform(df['tags']) # creamos la matriz donde estaran las palabras de cada tag y su frecuencia
```

Se creo una funcion que recibe el titulo de una pelicula y busca entre todo el dataset las que 5 que tengan mas palabras relacionadas de acuerdo al campo tags y las ordena mayor a menor similitud y las retorna.

```python
rec = recomendacion('Toy Story')
#  La respuesta de la funcion es:
La pelicula que viste es: Toy Story
Tu recomendacion es: 
1 - Toy Story 2
2 - Rebel Without A Cause
3 - The Thin Red Line
4 - Radio Days
5 - The Sunchaser
```

Nota: El dataset completo es de 45000 peliculas, para la implementacion del algoritmo solo se usa un muestro de 3000 ya que los recursos de maquina son limitados, por ende solo recomendara peliculas que esten dentro de esta muestra.

Si se cuenta con recursos de maquina superiores la recomendacion es mas acertada. 

Todo este proceso se encuentra en [Modelo ML](https://github.com/danser996/PI_DS/tree/master/code)

## **Desarrollo API**
## API
API es el acrónimo de "Application Programming Interface" (Interfaz de Programación de Aplicaciones). Se trata de un conjunto de reglas y protocolos que permite a diferentes aplicaciones y sistemas comunicarse e interactuar entre sí de manera estandarizada.

Una API define las funciones y métodos que una aplicación proporciona para que otros programas puedan utilizar sus servicios y acceder a sus datos de manera controlada. Funciona como una capa de abstracción que permite a los desarrolladores utilizar ciertas funcionalidades de una aplicación o servicio sin necesidad de conocer todos los detalles internos de su implementación.

<!-- ![API](/src/appmaster.avif) -->
<p align=center><img src=https://appmaster.io/cdn-cgi/image/width=768,quality=83,format=auto/api/_files/PqV7MuNwv89GrZvBd4LNNK/download/><p>

## FastAPI
Para desarrollar la API, se optó por utilizar FastAPI, un framework rápido y eficiente en Python. Se hizo uso del potencial del DataFrame de Python para manipular y analizar los datos necesarios.

![FastAPI](/src/FA.png)

## Render
Una vez completada la implementación y las pruebas, la API fue desplegada en la plataforma Render, que ofrece una infraestructura escalable y confiable para alojar aplicaciones web. Esta combinación de tecnologías permitió crear una API robusta y de alto rendimiento, capaz de procesar solicitudes y brindar respuestas eficientes a los usuarios. El despliegue en Render garantizó una disponibilidad constante y una buena experiencia de uso.

 ![Render](/src/RENDER.png)

Toda el desarrollo de la API se encuentra en el [Repositorio de la API](https://github.com/danser996/PI_DS).