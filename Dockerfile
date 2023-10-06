# pull the official base image
FROM python:3.11-alpine3.17

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
RUN pip install django requests pandas plotly steammarket CurrencyConverter bs4 pytz
RUN mkdir /precios

# copy project
COPY . /app/

CMD ["sh", "run.sh"]