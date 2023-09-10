FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./scheduling-api /code/scheduling-api

CMD ["uvicorn", "scheduling-api.main:app", "--host", "0.0.0.0", "--port", "80"]