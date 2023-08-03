FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN flask db init
RUN flask db migrate -m "init"
RUN flask db upgrade
RUN flask seed users

CMD [ "flask", "run" , "-h", "0.0.0.0", "-p", "80"]

EXPOSE 80/tcp
EXPOSE 443/tcp
