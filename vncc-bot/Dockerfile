# DOCKERFILE BOT-CLIENT
FROM python:3.10

EXPOSE 443
EXPOSE 80

WORKDIR /usr/app

COPY /src/bot.py ./
COPY /src/main.py ./
COPY /src/requirements.txt ./
COPY  /src/.env ./
RUN mkdir /usr/app/queries
RUN pip install -r requirements.txt



CMD ["python3", "./main.py"]



