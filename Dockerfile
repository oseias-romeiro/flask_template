FROM python

ENV APP_ENV=
ENV SECRET_KEY= 

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN flask db init
RUN flask db migrate -m "init"
RUN flask db upgrade
RUN flask seed users

CMD [ "gunicorn", "-b" , "0.0.0.0:80", "wsgi:app"]

EXPOSE 80/tcp
EXPOSE 443/tcp
