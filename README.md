# Proyecto ETL con Prefect

Este repositorio contiene ejemplos sencillos de procesos **Extract‑Transform‑Load (ETL)** implementados con [Prefect](https://www.prefect.io), la librería de orquestación de flujos de trabajo.

## 📁 Estructura del proyecto

- `ejercicio_cypress.py` – ETL que obtiene publicaciones de la API de Cypress (JSONPlaceholder) y las guarda en una base de datos SQLite.
- `pydata_denver.py` – ETL que descarga las últimas quejas de consumidores desde la API de la CFPB, las transforma y las persiste también en SQLite.

## 🚀 Requisitos

- Python 3.8+  
- Dependencias (instalables con `pip`):

  ```sh
  pip install prefect requests
  ```

> 💡 Si utilizas un entorno virtual (recomendado), créalo y actívalo antes de instalar las librerías.

## 🛠️ Descripción de los flujos

### `ejercicio_cypress.py`

1. **Extract**: recupera posts desde `https://jsonplaceholder.cypress.io/posts`.
2. **Transform**: filtra los 15 primeros y normaliza los campos (`userId`, `id`, `title`).
3. **Load**: crea/actualiza la tabla `posts` en `cypress_data.db` y almacena los registros.

### `pydata_denver.py`

1. **Extract**: consulta la API de quejas de consumidores de la CFPB con parámetro `size=10`.
2. **Transform**: extrae campos relevantes (`date_recieved`, `state`, `product`, etc.).
3. **Load**: crea la tabla `complaint` en `cfpbcomplaints.db` y vuelca los datos.

Ambos scripts definen flujos de Prefect (`Flow`) que se ejecutan directamente al invocarlos como programas (`python script.py`).

## 🧪 Ejecución

Desde la raíz del proyecto:

```sh
python ejercicio_cypress.py
python pydata_denver.py
```

Cada ejecución crea (o actualiza) el fichero SQLite correspondiente en el directorio de trabajo.

## 📦 Salidas

- `cypress_data.db` – contiene la tabla `posts`.
- `cfpbcomplaints.db` – contiene la tabla `complaint`.

Puedes inspeccionarlos con cualquier cliente SQLite (`sqlite3`, DB Browser for SQLite, etc.).

## 🤝 Contribuciones

¡Bienvenidas! Si deseas ampliar el proyecto, añadir más fuentes, o integrar un servidor de Prefect Cloud/Server, abre un _issue_ o envía un _pull request_.

## 📝 Licencia

Este proyecto se proporciona "tal cual", sin garantía expresa. Úsalo libremente para aprender o como punto de partida para tus propios flujos ETL.

---

🔧 **Tip**: modifica los scripts para parametrizar URLs y tamaños de lote, o convierte los flujos en tareas de un `Deployment` de Prefect para ejecución programada.

---