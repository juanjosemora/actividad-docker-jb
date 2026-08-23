FROM python:3.9-slim
WORKDIR /app
RUN echo "print('Hola desde Docker Actions')" > app.py
CMD ["python", "app.py"]
