from bottle import Bottle, run
import datetime
import re
import subprocess

app = Bottle()

@app.route('/')
def default():
    return """<!DOCTYPE html>
        <html>
        <head>
        <title>Bienvenido a nuestra página web!</title>
        <style>
        html { color-scheme: light dark; }
        body { 
            width: 35em; 
            margin: 0 auto;
            font-family: Tahoma, Verdana, Arial, sans-serif; 
            background-color: white !important; /* Fondo blanco forzado */
        }
        h1, h2 { color: #333; }
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #333;
            padding: 10px 0;
            border-bottom: 2px solid #06c;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            z-index: 1000;
        }
        .navbar button {
            background-color: #06c;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
        }
        .navbar button:hover {
            background-color: #0056b3;
        }
        .content {
            background: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            border: 2px solid #ccc;
            margin-top: 80px; /* Para evitar que el contenido se solape con la barra de navegación */
            text-align: center;
        }
        .image-container {
            text-align: center;
            margin-top: 20px;
        }
        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }
        .footer {
            margin-top: 20px;
            font-size: 0.9em;
            color: #666;
            text-align: center;
        }
        </style>
        <script>
        function redirectTo(path) {
            window.location.href = path;
        }
        </script>
        </head>
        <body>
        <div class="navbar">
            <button onclick="redirectTo('/hi')">Hora</button>
            <button onclick="redirectTo('/status')">Servicios</button>
        </div>
        <div class="content">
        <h2>Bienvenido a la web de Pablo y Marinela</h2>
        <h2>Sistemas Operativos - Grado en Inteligencia Artificial</h2>
        <h3>Práctica 1</h3>
        </div>
        <div class="footer">
        <p>© 2025 Pablo y Marinela </p>
        </div>
        </body>
        </html>"""

@app.route('/hi')
def hi():
    return """<!DOCTYPE html>
        <html>
        <head>
        <title>Hora Actual</title>
        <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #333;
            padding: 10px 0;
            border-bottom: 2px solid #06c;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            z-index: 1000;
        }
        .navbar button {
            background-color: #06c;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
        }
        .navbar button:hover {
            background-color: #0056b3;
        }
        .clock-container {
            text-align: center;
            margin-top: 60px; /* Para evitar que el contenido se solape con la barra de navegación */
        }
        .clock {
            font-size: 5rem;
            font-weight: bold;
            color: #333;
            cursor: pointer;
        }
        .greeting {
            font-size: 2rem;
            color: #666;
        }
        .analog-clock {
            display: none;
            width: 200px;
            height: 200px;
            border: 10px solid #333;
            border-radius: 50%;
            position: relative;
            margin: 20px auto;
        }
        .hand {
            position: absolute;
            background-color: #333;
            transform-origin: 50% 100%; /* Rotación desde el centro inferior */
            transition: all 0.05s;
            transition-timing-function: cubic-bezier(0.1, 2.7, 0.58, 1);
        }
        .hour-hand {
            width: 6px;
            height: 50px; /* Longitud de la manecilla de horas */
            top: 50px; /* Posición desde el centro */
            left: 97px; /* Centrado horizontal */
        }
        .minute-hand {
            width: 4px;
            height: 70px; /* Longitud de la manecilla de minutos */
            top: 30px; /* Posición desde el centro */
            left: 98px; /* Centrado horizontal */
        }
        .second-hand {
            width: 2px;
            height: 90px; /* Longitud de la manecilla de segundos */
            top: 10px; /* Posición desde el centro */
            left: 99px; /* Centrado horizontal */
            background-color: red;
        }
        </style>
        <script>
        function updateClock() {
            const now = new Date();
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;

            const hourHand = document.getElementById('hour-hand');
            const minuteHand = document.getElementById('minute-hand');
            const secondHand = document.getElementById('second-hand');

            const hour = now.getHours() % 12;
            const minute = now.getMinutes();
            const second = now.getSeconds();

            const hourDeg = (hour * 30) + (minute * 0.5); // Grados para la manecilla de horas
            const minuteDeg = (minute * 6) + (second * 0.1); // Grados para la manecilla de minutos
            const secondDeg = second * 6; // Grados para la manecilla de segundos

            hourHand.style.transform = `rotate(${hourDeg}deg)`;
            minuteHand.style.transform = `rotate(${minuteDeg}deg)`;
            secondHand.style.transform = `rotate(${secondDeg}deg)`;
        }
        setInterval(updateClock, 1000);
        window.onload = updateClock;

        function toggleAnalogClock() {
            const analogClock = document.getElementById('analog-clock');
            if (analogClock.style.display === 'none') {
                analogClock.style.display = 'block';
            } else {
                analogClock.style.display = 'none';
            }
        }

        function redirectTo(path) {
            window.location.href = path;
        }
        </script>
        </head>
        <body>
        <div class="navbar">
            <button onclick="redirectTo('/')">Inicio</button>
            <button onclick="redirectTo('/status')">Servicios</button>
        </div>
        <div class="clock-container">
            <div id="clock" class="clock" onclick="toggleAnalogClock()"></div>
            <div class="greeting">Hola, hoy es <span id="date"></span></div>
            <div id="analog-clock" class="analog-clock">
                <div id="hour-hand" class="hand hour-hand"></div>
                <div id="minute-hand" class="hand minute-hand"></div>
                <div id="second-hand" class="hand second-hand"></div>
            </div>
        </div>
        <script>
        const now = new Date();
        const dateString = now.toLocaleDateString('es-ES', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
        document.getElementById('date').textContent = dateString;
        </script>
        </body>
        </html>"""

@app.route('/status')
def status():
    try:
        # Ejecutar el comando para listar los servicios en sistemas basados en Unix
        services = subprocess.check_output("service --status-all", shell=True).decode('utf-8')
        services_list = services.splitlines()
    except Exception as e:
        services_list = [f"Error al obtener servicios: {str(e)}"]

    # Crear elementos de lista para los servicios
    services_html = ""

    for service in services_list:
        service = service.strip()
        match = re.match(r"\[\s*([+-])\s*\]\s*(.+)", service)

        if match:
            estado = match.group(1).strip()  # Estado (+ o -)
            nombre_servicio = match.group(2).strip()  # Nombre del servicio
            color = "#4DAA57" if estado == "+" else "#D73533"  # Verde si activo, rojo si inactivo
        else:
            estado = "?"
            nombre_servicio = service
            color = "gray"  # Color por defecto si el estado es desconocido

        # Agregar cada servicio con su icono de estado
        services_html += f"""
        <div class="service-item">
            <div class="status-circle" style="background-color: {color};"></div>
            <span>{nombre_servicio}</span>
        </div>
        """

    # Plantilla HTML con el nuevo diseño
    html_page = f"""
    <!DOCTYPE html>
    <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Servicios</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    padding: 20px;
                    background-color: #f4f4f4;
                    text-align: center;
                }}
                h1 {{
                    text-align: center;
                }}
                .services-container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    margin-top: 20px;
                }}
                .service-item {{
                    display: flex;
                    align-items: center;
                    background: white;
                    padding: 10px;
                    margin: 5px;
                    width: 50%;
                    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }}
                .status-circle {{
                    width: 15px;
                    height: 15px;
                    border-radius: 50%;
                    margin-right: 15px;
                }}
                .navbar {{
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    background-color: #333;
                    padding: 10px 0;
                    border-bottom: 2px solid #06c;
                    display: flex;
                    justify-content: flex-start;
                    align-items: center;
                    z-index: 1000;
                }}
                .navbar button {{
                    background-color: #06c;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    margin: 0 10px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 1rem;
                }}
                .navbar button:hover {{
                    background-color: #0056b3;
                }}
                .content {{
                    margin-top: 80px;
                }}
            </style>
            <script>
            function redirectTo(path) {{
                window.location.href = path;
            }}
            </script>
        </head>
        <body>
            <div class="navbar">
                <button onclick="redirectTo('/')">Inicio</button>
                <button onclick="redirectTo('/hi')">Hora</button>
            </div>
            <div class="content">
                <h1>Servicios en el Servidor</h1>
                <div class="services-container">
                    {services_html}
                </div>
            </div>
        </body>
    </html>
    """

    return html_page

if __name__ == "__main__":
    run(app, host='0.0.0.0', port=8080)

