# 🔍 IG Followers

Este proyecto en Python te permite analizar tus datos descargados desde Instagram para identificar qué usuarios sigues pero que no te siguen de vuelta.

## 📦 ¿Qué hace?

- Lee los archivos `.zip` que proporciona Instagram cuando descargas tu información.
- Extrae la lista de personas que sigues y las que te siguen.
- Detecta los usuarios que **no te siguen de vuelta**.
- Devuelve un DataFrame con el nombre de usuario y su enlace directo a Instagram.

## 🐍 Tecnologías utilizadas

- Python
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) para el parsing de HTML.
- [pandas](https://pandas.pydata.org/) para la manipulación de datos.
- `zipfile` y `pathlib` para trabajar con archivos comprimidos.

## 🗂️ Estructura esperada del archivo de Instagram

Debes descargar tu información desde la app de Instagram. Asegúrate de **solicitar el formato HTML** (no JSON).

1. Ve a Instagram → Tu perfil → Tu actividad → Descargar tu información.

2. El archivo `.zip` contendrá carpetas como:
    - followers_and_following/
    - following.html
    - followers_1.html


⚠️ **Notas**
- Este proyecto no interactúa con la API de Instagram.

- Solo funciona con los archivos descargados por el usuario desde Instagram.

- No se recopila ni almacena ninguna información personal.

---

