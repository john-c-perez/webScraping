Scraping con Scrapy

Este repositorio contiene un proyecto de scraping utilizando Scrapy, un framework de Python para la extracción de datos de sitios web de manera eficiente y estructurada.

📌 Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

Python 3.7 o superior (Descargar aquí)

pip (gestor de paquetes de Python)

Scrapy (instalable con pip)

🚀 Instalación

1️⃣ Clonar el repositorio

git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

2️⃣ Crear un entorno virtual (opcional pero recomendado)

python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows

3️⃣ Instalar Scrapy

pip install scrapy

🔧 Configuración y ejecución

1️⃣ Verificar la instalación de Scrapy

scrapy version

Si hay un error, verifica que Python y Scrapy están en el PATH.

En Windows, si Scrapy no se ejecuta correctamente, prueba:

python -m scrapy

O ejecuta el archivo scrapy.exe directamente desde:

direccion\proyecto\scrapy.exe startproject nombre_proyecto

2️⃣ Crear un nuevo proyecto Scrapy

scrapy startproject nombre_proyecto
cd nombre_proyecto

3️⃣ Crear un spider

Dentro de la carpeta spiders, crea un archivo Python para tu Spider. Por ejemplo, noticias_spider.py. 

4️⃣ Ejecutar el spider

scrapy crawl nombre_spider

Si deseas guardar los datos en un archivo JSON o CSV:

scrapy crawl nombre_spider -o datos.json
scrapy crawl nombre_spider -o datos.csv

🛠 Solución de problemas

Scrapy no reconocido como comando: Añadir el directorio de Python y Scripts al PATH.

Errores de permisos en Windows: Ejecutar la terminal como Administrador.

Error de importación de Scrapy: Verifica que estás en el entorno virtual correcto.

📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

¡Contribuciones y sugerencias son bienvenidas! 😊
