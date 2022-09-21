# pull official base image
FROM python:3.8

# Setup some other prereqs needed:
RUN apt-get update && apt-get --assume-yes install imagemagick ghostscript sqlite3


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

COPY docker-entrypoint.sh docker-entrypoint.sh

# create the app user
# RUN addgroup --system app && adduser --system app --group app

# RUN chown -R app:app 

# change to the app user
# USER app
RUN chmod +x ./docker-entrypoint.sh

# ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["./docker-entrypoint.sh"] 