import os

from app import crear_servidor_archivos


settings_module = os.getenv('APP_SETTINGS_MODULE', 'config.dev')
port_grpc = os.getenv('GRPC_PORT', 5001)
ip_mongod_server = os.getenv('MONGO_IP', "127.0.0.1")
ip_convertidor_archivos = os.getenv('CONVERTIDOR_ARCHIVOS_IP', "127.0.0.1")
port_convertidor_archivos = os.getenv('CONVERTIDOR_ARCHIVOS_PORT', 5002)

grp_server = crear_servidor_archivos(puerto=port_grpc, direccion_convertidor=ip_convertidor_archivos, puerto_convertidor=port_convertidor_archivos, ip_servidor_mongo=ip_mongod_server)