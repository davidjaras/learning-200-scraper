# learning-200-scraper

Web scraping de cursos completados por estudiante de platzi.
Consumo a través de API Flask con un solo endpoint

  
### Directorio de archivos

/scraper  
	---- config.py  
	---- functions.py 
    ---- main.py   
	---- scraper.py  


### Entorno virtual

Instalación en windows:
> python -m venv venv

Activación del entorno
> venv\Scripts\activate


##### Librerías necesarias:

Requests:
> pip install requests

BeautifulSoup
> pip install beautifulsoup4

Flask
> pip install flask



### Forma de uso

En el directorio /scraper ejecutar a través de comandos:
> python main.py
  
Esto pone en ejecución la app de Flask que contiene la api.

#### Api Endpoints:

Obtener cursos:
>http://[direccion_IP]:5000/api/[Usuario_de_platzi]

#### Respuesta:
Salida en formato json con dos atributos: *message* y *courses*

###### Tipos de message
- Consulta exitosa
*message* : OK: 200

- perfil privado o no tiene cursos aprobados
*message* : Profile is private or has not approved courses

- perfil inexistente o error de requests
*message* : 'Fail. Status code: [http_status_code]

#### Ejemplo:
Input:
> http://127.0.0.1:5000/api/davidjaras

Output:
>{
  "courses": [
    {
      "approved": true, 
      "badge": "https://static.platzi.com/media/achievements/1301-97adc02b-c21c-46fc-b753-c50bf1a98f67.png", 
      "career": "Fundamentos de Programaci\u00f3n", 
      "color": "#95c73f", 
      "completed": 100, 
      "deprecated": false, 
      "diploma": null, 
      "diploma_link": "/p/davidjaras/curso/1301-expresiones-regulares/diploma/detalle/", 
      "exam_url": null, 
      "has_exam": "39afb522-97f5-4b24-8c42-3bfa1d913f7f", 
      "id": 1301, 
      "image": "https://static.platzi.com/media/achievements/platzi-bd.png", 
      "material_seen": 0, 
      "slug": "expresiones-regulares", 
      "title": "Curso de Expresiones Regulares", 
      "total_material": 0, 
      "url": "/clases/expresiones-regulares/"
    },
    {
      "approved": true, 
      "badge": "https://static.platzi.com/media/achievements/badge-fundamentos-web-scraping-python-1578d3cc-5f38-4c53-981e-7f4ba3f4b801.png", 
      "career": "Desarrollo Backend con Python y Django", 
      "color": "#23a311", 
      "completed": 100, 
      "deprecated": false, 
      "diploma": null, 
      "diploma_link": "/p/davidjaras/curso/1908-web-scraping/diploma/detalle/", 
      "exam_url": null, 
      "has_exam": "f586f220-34a4-4591-9d39-26a95bcb8348", 
      "id": 1908, 
      "image": "https://static.platzi.com/media/achievements/platzi-bd.png", 
      "material_seen": 0, 
      "slug": "web-scraping", 
      "title": "Curso de Fundamentos de Web Scraping con Python y Xpath", 
      "total_material": 0, 
      "url": "/clases/web-scraping/"
    },
  ], 
  "message": "OK: 200"
}