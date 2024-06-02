FROM  python:3.12-slim


WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN cd api/
ENTRYPOINT ["python", "api/main.py"]


# command to build:
# docker build -t fastapi .

# command to run
# docker run -v $(pwd):/app/ -p 8000:8000 -it --name fastapi --rm fastapi