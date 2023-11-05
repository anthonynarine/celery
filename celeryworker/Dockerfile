FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# prevent python writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1 
# ensure Python output is set direct to the terminal without buffering 
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

