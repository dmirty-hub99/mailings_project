FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir code
WORKDIR code

ADD . /code/

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "8080"]
