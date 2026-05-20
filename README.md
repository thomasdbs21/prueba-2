# Proyecto DevOps - Sistema Climático para Pilotos

## Descripción

Este proyecto consiste en una aplicación desarrollada en Python que consume una API meteorológica para obtener información climática en tiempo real.

La aplicación está orientada a pilotos de avión y personal aeronáutico, permitiendo consultar las condiciones climáticas antes de un vuelo para determinar si existen condiciones adecuadas para despegar o aterrizar de forma segura.

La solución fue containerizada utilizando Docker y automatizada mediante Jenkins Pipeline aplicando conceptos DevOps y CI/CD.

---

# Stakeholder

La solución está dirigida a:

- Pilotos de avión
- Personal aeronáutico
- Torres de control
- Equipos de monitoreo climático
- Aerolíneas

---

# Problema Detectado

Las condiciones climáticas afectan directamente la seguridad aérea.

Factores como:

- temperatura
- humedad
- viento
- tormentas
- visibilidad

pueden impedir o dificultar un vuelo.

La revisión manual constante de datos meteorológicos puede generar:
- retrasos
- errores humanos
- falta de automatización
- decisiones tardías

---

# Solución Implementada

Se desarrolló una aplicación automatizada capaz de:

- consultar datos climáticos en tiempo real
- mostrar temperatura, humedad y velocidad del viento
- ejecutar la aplicación mediante contenedores Docker
- automatizar despliegues utilizando Jenkins Pipeline
- utilizar variables de entorno para proteger credenciales API

---

# Tecnologías Utilizadas

- Python 3
- Docker
- Jenkins
- GitHub
- Linux Ubuntu / DEVASC VM
- API OpenWeather

---

# Estructura del Proyecto

```text
clima-app/
├── app.py
├── build.sh
├── requirements.txt
├── README.md
├── evidencias/
│   ├── docker/
│   └── jenkins/
