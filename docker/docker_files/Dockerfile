# install python
FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -e; \
    apt-get update ;\
    apt-get -y install netcat-openbsd ;\
    apt-get -y install gettext ;

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./docker/entrypoints/entrypoint.sh ;

EXPOSE 8080
ENTRYPOINT ["./docker/entrypoints/entrypoint.sh"]

# LABEL org.opencontainers.image.source=https://github.com/aftanza/test-server