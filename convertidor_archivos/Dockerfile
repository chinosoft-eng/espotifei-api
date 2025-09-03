FROM python:3.11.13-slim
WORKDIR /usr/src/app
COPY . .
RUN apt-get update
RUN apt-get install -y ffmpeg build-essential python3-dev g++
RUN pip3 install -r requerimientos.txt
RUN python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/ConvertidorDeArchivos.proto
RUN touch EspotifeiConvertidorDeArchivos.log
EXPOSE 5002
CMD ["python3", "ConvertidorDeArchivosServer.py"]
