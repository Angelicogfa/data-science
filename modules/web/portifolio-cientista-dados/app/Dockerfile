FROM python:3

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./startup.py" ]
EXPOSE 5000