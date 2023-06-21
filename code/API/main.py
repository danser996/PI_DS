# importacion de modelos requeridos
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# cargamos base de datos como dataframe
# data = pd.read_csv("D:\DataScience\PI\Process\Dataset_def\dt_movies.csv", index_col=0)
# print(data)

# cambiar a tipo fecha la columna release_Date
# data.release_date = pd.to_datetime(data.release_date)

# realizamos la validacion de datos por pydantic y hara que los tipo de dato sean coherentes
class Validation(BaseModel):
    titulo:str
    nombre_actor:str
    nombre_director:str
    año:int
    mes:str
    dia:str
    
app = FastAPI()

## funciones API proyecto individual
@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes:Validation):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas 
    que se estrenaron ese mes historicamente'''
    return {'mes':mes, 'cantidad':respuesta}

@app.get('/cantidad_filmaciones_dia{dia}')
def cantidad_filmaciones_dia(dia:Validation):
    '''Se ingresa el dia y la funcion retorna la cantidad de 
    peliculas que se estrebaron ese dia historicamente'''
    return {'dia':dia, 'cantidad':respuesta}

@app.get('/score_titulo/{titulo}')
def score_titulo(titulo:Validation):
    '''Se ingresa el título de una filmación esperando como respuesta 
    el título, el año de estreno y el score'''
    return {'titulo':titulo, 'anio':respuesta, 'popularidad':respuesta}

@app.get('/votos_titulo/{titulo}')
def votos_titulo(titulo:Validation):
    '''Se ingresa el título de una filmación esperando como respuesta el título, 
    la cantidad de votos y el valor promedio de las votaciones. 
    La misma variable deberá de contar con al menos 2000 valoraciones, 
    caso contrario, debemos contar con un mensaje avisando que no cumple 
    esta condición y que por ende, no se devuelve ningun valor.'''
    return {'titulo':titulo, 'anio':respuesta, 'voto_total':respuesta, 'voto_promedio':respuesta}

@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor:Validation):
    '''Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo 
    devolver el éxito del mismo medido a través del retorno. 
    Además, la cantidad de películas que en las que ha participado y el promedio de retorno'''
    return {'actor':nombre_actor, 'cantidad_filmaciones':respuesta, 'retorno_total':respuesta, 'retorno_promedio':respuesta}

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:Validation):
    ''' Se ingresa el nombre de un director que se encuentre dentro de un dataset 
    debiendo devolver el éxito del mismo medido a través del retorno. 
    Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, 
    retorno individual, costo y ganancia de la misma.'''
    return {'director':nombre_director, 'retorno_total_director':respuesta, 
    'peliculas':respuesta, 'anio':respuesta,, 'retorno_pelicula':respuesta, 
    'budget_pelicula':respuesta, 'revenue_pelicula':respuesta}

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:Validation):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    return {'lista recomendada': respuesta}







## prueba API
@app.get("/") # "/" se refiere a http://127.0.0.1:8000 
def index():
    return {"message" : "Hola"}

@app.get("/libros/{id}")
def mostrar_libro(id:int):
    return {'data': id}

@app.post("/libros")
def insertar_libro(libro:Libro):
    return {"message": f"libro {libro.titulo} insertado"}

