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
<img width="993" height="192" alt="image" src="https://github.com/user-attachments/assets/ddcb5048-b27f-4a7b-b9a3-bf974948d4cc" />
<img width="858" height="524" alt="image" src="https://github.com/user-attachments/assets/79aa5224-98ed-43e4-a0ec-49554022e9b8" />

### `pydata_denver.py`

1. **Extract**: consulta la API de quejas de consumidores de la CFPB con parámetro `size=10`.
2. **Transform**: extrae campos relevantes (`date_recieved`, `state`, `product`, etc.).
3. **Load**: crea la tabla `complaint` en `cfpbcomplaints.db` y vuelca los datos.
<img width="991" height="173" alt="image" src="https://github.com/user-attachments/assets/6a00e69c-5e6d-4571-b337-6121b9e13495" />
<img width="1277" height="649" alt="image" src="https://github.com/user-attachments/assets/c6d6a027-4178-4cd0-a4e7-73e7fb14461f" />


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
<img width="858" height="524" alt="image" src="https://github.com/user-attachments/assets/79aa5224-98ed-43e4-a0ec-49554022e9b8" />
- `cfpbcomplaints.db` – contiene la tabla `complaint`.
<img width="1277" height="649" alt="image" src="https://github.com/user-attachments/assets/c6d6a027-4178-4cd0-a4e7-73e7fb14461f" />

Puedes inspeccionarlos con cualquier cliente SQLite (`sqlite3`, DB Browser for SQLite, etc.).

## 🤝 Contribuciones

¡Bienvenidas! Si deseas ampliar el proyecto, añadir más fuentes, o integrar un servidor de Prefect Cloud/Server, abre un _issue_ o envía un _pull request_.

## 📝 Licencia

Este proyecto se proporciona "tal cual", sin garantía expresa. Úsalo libremente para aprender o como punto de partida para tus propios flujos ETL.

---

🔧 **Tip**: modifica los scripts para parametrizar URLs y tamaños de lote, o convierte los flujos en tareas de un `Deployment` de Prefect para ejecución programada.

---
