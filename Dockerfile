FROM python:3.8.0
EXPOSE 3000
WORKDIR /src
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
COPY ./req.txt req.txt
RUN pip install -r req.txt
COPY ./project/ ./project/
WORKDIR /src/project