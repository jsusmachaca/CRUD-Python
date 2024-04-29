FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install tk pymysql python-dotenv

CMD [ "python", "main.py" ]