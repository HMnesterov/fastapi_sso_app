FROM python:3.11-alpine

COPY ./requirements /backend/requirements

RUN pip install -r ./backend/requirements/req-prod.txt

COPY . /backend/

WORKDIR /backend/

ENTRYPOINT ["python", "main.py"]


