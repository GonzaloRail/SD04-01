Claro, aquí tienes un `README.md` detallado que te guía paso a paso para ejecutar tu proyecto Flask con llamadas RPC usando RabbitMQ (en Docker) y exponerlo con Ngrok:

---

# 🚀 Proyecto Flask + RabbitMQ + RPC + Ngrok

Este proyecto demuestra cómo usar **Flask** con llamadas **RPC asíncronas** a través de **RabbitMQ**, y exponer la aplicación web al mundo usando **Ngrok**.

---

## 📦 Requisitos

* Python 3.x
* Docker (para correr RabbitMQ)
* Ngrok (para exponer localmente tu app)
* Git (opcional)

---

## ⚙️ Instalación

### 1. Clona o descarga este repositorio

```bash
git clone https://github.com/tu-usuario/rpc-flask-ngrok.git
cd rpc-flask-ngrok
```

### 2. Instala dependencias de Python

```bash
pip install flask amqpstorm
```

---

## 🐇 Levanta RabbitMQ con Docker

```bash
docker run -d --hostname my-rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

* Accede a RabbitMQ en tu navegador: [http://localhost:15672](http://localhost:15672)
* Usuario: `guest`
* Contraseña: `guest`

---

## 🧠 Ejecuta el Servidor RPC

Abre una terminal y ejecuta:

```bash
python rpc_server.py
```

Este script escucha solicitudes desde Flask y responde con un mensaje personalizado.

---

## 🌐 Ejecuta Flask

En otra terminal, ejecuta:

```bash
python app.py
```

Esto inicia el servidor en `http://127.0.0.1:5000`

---

## 🌍 Exponer con Ngrok

### 1. Descarga y configura Ngrok

Descarga desde: [https://ngrok.com/download](https://ngrok.com/download)

Autentica tu cuenta (solo la primera vez):

```bash
ngrok config add-authtoken TU_AUTHTOKEN
```

### 2. Ejecuta Ngrok

```bash
ngrok http 5000
```

Ngrok mostrará una URL pública como:

```
Forwarding    https://abcd-1234.ngrok-free.app -> http://localhost:5000
```

📎 Usa esa URL para compartir tu app en la web.

---

## 🖼️ Interfaz Web

Cuando entres a la URL pública o `http://localhost:5000` verás una interfaz con Bootstrap donde puedes escribir un mensaje.
Al enviar, Flask lo envía al servidor RPC, y te muestra la respuesta.

---

## 📁 Estructura del Proyecto

```
.
├── app.py               # Servidor Flask
├── rpc_server.py        # Servidor RPC que responde mensajes
├── templates/
│   └── index.html       # Interfaz web con Bootstrap
└── README.md            # Guía de instalación y ejecución
```


