# learning-200-scraper

Web scraping de cursos completados por estudiante de platzi

  
### Directorio de archivos

/scraper
	----config.py
	----functions.py
	----scraper.py
  
  ### Entorno virtual

Instalación en windows:

> python -m venv venv

  

Activación del entorno

> venv\Scripts\activate

  

#####Librerías necesarias:

  

Requests:

> pip install requests

  

BeautifulSoup

> pip install beautifulsoup4

### Forma de uso

  

En el directorio /scraper ejecutar a través de comandos:

> python scraper.py [Usuario_de_platzi>]

#### Respuesta:
Salida en formato json con dos atributos: *message* y *courses*

#### Ejemplo:
Input:
> python scraper.py davidjaras

Output:
>{'message': 'OK: 200', 'courses': [ {'id': 1566, 'title': 'Fundamentos de Bases de Datos', 'slug': 'bd', 'image': 'https://static.platzi.com/media/achievements/platzi-bd.png', 'color': '#95c73f', 'badge': 'https://static.platzi.com/media/achievements/badge-fundamentos-de-bases-de-datos-cc5eff2a-a7e0-4110-af5d-a47b628611da.png', 'url': '/clases/bd/', 'approved': True, 'diploma': None, 'completed': 100, 'career': 'Big Data y Data Science', 'deprecated': False, 'diploma_link': '/p/davidjaras/curso/1566-bd/diploma/detalle/', 'exam_url': None, 'material_seen': 0, 'total_material': 0, 'has_exam': '1b6f0665-e84a-4e60-9ebf-d7e4d46f7b79'}, {'id': 1937, 'title': 'Curso Básico de Python', 'slug': 'python', 'image': 'https://static.platzi.com/media/achievements/platzi-bd.png', 'color': '#23a311', 'badge': 'https://static.platzi.com/media/achievements/badge-basico-python-bdcc67b3-031d-4dce-8e78-5699fb243149.png', 'url': '/clases/python/', 'approved': True, 'diploma': None, 'completed': 100, 'career': None, 'deprecated': False, 'diploma_link': '/p/davidjaras/curso/1937-python/diploma/detalle/', 'exam_url': None, 'material_seen': 0, 'total_material': 0, 'has_exam': '9ff2b8bb-1926-48bf-a885-a49d6cee9b4f'}]}