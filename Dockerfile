FROM python:3.10.12

ENV APP_PATH="/src/app" \
    APP="app"


WORKDIR /src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

COPY ${APP} ${APP_PATH}

CMD [ "python", "main.py" ]