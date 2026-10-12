# obesity-risk-mlops
**Objetivo:** 

Desarrollo de una solución end-to-end basada en MLOps para la estimación del riesgo de obesidad integrando análisis exploratorio de datos (EDA), pipelines reproducibles de machine learning, tracking de experimentos con MLflow y empaquetamiento en un microservicio desplegable mediante FastAPI y Docker

**Configuración del Entorno:**

Este proyecto fue desarrollado utilizando Python y herramientas de MLOps orientadas a garantizar reproducibilidad y facilidad de despliegue.

Requisitos Previos

Antes de ejecutar el proyecto asegúrate de tener instalado:

Git
Python 3.10 o superior
Visual Studio Code (recomendado)
Extensión Jupyter para VS Code

**Requisitos Previos** 

-Antes de ejecutar el proyecto asegúrate de tener instalado:

Git

Python 3.10 o superior

Visual Studio Code (recomendado)

Extensión Jupyter para VS Code

**Clonar el repositorio**

git clone https://github.com/acaropi/obesity-risk-mlops.git

cd obesity-risk-mlops

**Crear Entorno Virtual**
**Windows (PowerShell)**

python -m venv .venv

.\.venv\Scripts\activate

**MacOS / Linux**

python -m venv .venv

source .venv/bin/activate

**Instalación de Dependencias**

-Las dependencias del proyecto se encuentran definidas en el archivo:

requirements.txt

-Para instalarlas:

pip install -r requirements.txt

**Verificación del Entorno**

-Validar que la instalación fue correcta:

python --version

pip --version

**Ejecución del Notebook**

-Abrir Visual Studio Code y seleccionar:

notebooks/obesity_mlops.ipynb

-o abrir directamente el archivo:

obesity_mlops.ipynb

-Seleccionar el Kernel correspondiente al entorno virtual:

.venv

-Posteriormente ejecutar:

Run All

**Ejecución de la API**

-Para iniciar el servicio de predicción:

uvicorn app:app --reload

-La API quedará disponible en:

http://localhost:8000

**Documentación Automática**

FastAPI genera automáticamente documentación interactiva en:

http://localhost:8000/docs

**Ejecución con Docker**

docker build -t obesity-risk-api .

**Ejecutar Contenedor:**

docker run -p 8000:8000 obesity-risk-api

**Ejecución de Pruebas**

pytest

**Reproducibilidad**

Para garantizar la reproducibilidad del proyecto se implementaron las siguientes prácticas:

Uso de semilla fija (RANDOM_STATE = 52).
Versionamiento mediante Git y GitHub.
Gestión centralizada de dependencias mediante requirements.txt.
Tracking de experimentos con MLflow.
Orquestación de tareas con Prefect.
Containerización mediante Docker.
Pruebas unitarias para validación del pipeline.
