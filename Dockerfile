FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# eliminar el main.py que viene en la imagen
RUN rm -f main.py run.py

RUN pytest -v -s

# docker build -t api_demo1 .
# docker run -d -p 8084:80 api_demo1