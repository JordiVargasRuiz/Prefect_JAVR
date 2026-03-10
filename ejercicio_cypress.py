import requests
import json
from collections import namedtuple
from contextlib import closing
import sqlite3
from prefect import task, Flow

##1.EXTRACT: Obtener posts de la API de Cypress
@task
def extract_cypress_posts():
    """
    Extrae publicaciones desde JSONPlaceholder (Cypress).
    """
    url = "https://jsonplaceholder.cypress.io/posts"
    r = requests.get(url)
    return r.json()

##2.TRANSFORM: Limpiar los datos
@task
def transform_posts(raw_data):
    """
    Convierte el JSON a una lista de tuplas con nombre.
    """
    processed_posts = []
    #Definimos la estructura: ID del usuario, ID del post y el Título
    Post = namedtuple('Post', ['userId', 'id', 'title'])
    
    for item in raw_data:
        #Solo tomamos los primeros 15 para el ejemplo
        if len(processed_posts) < 15:
            new_post = Post(
                userId=item.get('userId'),
                id=item.get('id'),
                title=item.get('title')
            )
            processed_posts.append(new_post)
    return processed_posts

##3.LOAD: Guardar en una nueva base de datos
@task
def load_to_db(data):
    """
    Crea la tabla y guarda los posts en cypress_data.db.
    """
    create_sql = 'CREATE TABLE IF NOT EXISTS posts (user_id INTEGER, post_id INTEGER, title TEXT)'
    insert_sql = "INSERT INTO posts VALUES (?, ?, ?)"
    
    with closing(sqlite3.connect("cypress_data.db")) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(create_sql)
            cursor.executemany(insert_sql, data)
            conn.commit()
    print(f"Se han guardado {len(data)} registros en cypress_data.db")

#DEFINICIÓN DEL FLOW
with Flow("Cypress ETL Workflow") as f:
    datos_crudos = extract_cypress_posts()
    datos_limpios = transform_posts(datos_crudos)
    load_to_db(datos_limpios)

if __name__ == "__main__":
    f.run()