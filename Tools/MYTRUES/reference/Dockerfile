FROM python:3.13-alpine
WORKDIR /app
COPY engine_port.py cases.py server.py ./
COPY fixtures ./fixtures
EXPOSE 8080
CMD ["python", "server.py"]
