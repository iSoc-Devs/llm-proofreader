FROM python:3.12.7

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./.env /code/.env

COPY ./main.py /code/main.py

CMD ["fastapi", "run", "main.py", "--port", "80"]