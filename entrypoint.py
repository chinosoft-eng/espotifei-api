# Por ejemplo, APP_SETTINGS_MODULE = config.prod
import os

from app import create_app
settings_module = os.getenv('APP_SETTINGS_MODULE', 'config.dev')
port_grpc = os.getenv('GRPC_PORT', 5001)
ip_mongod_server = os.getenv('MONGO_IP', "127.0.0.1")
ip_convertidor_archivos = os.getenv('CONVERTIDOR_ARCHIVOS_IP', "127.0.0.1")
port_convertidor_archivos = os.getenv('CONVERTIDOR_ARCHIVOS_PORT', 5002)
app = create_app(settings_module, puerto_convertidor=port_convertidor_archivos,
                 direccion_convertidor=ip_convertidor_archivos, puerto=port_grpc, ip_servidor_mongo=ip_mongod_server,
                 iniciar_grcp_server=False)

app.run("0.0.0.0", 5000)