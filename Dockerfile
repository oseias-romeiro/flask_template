FROM python

ENV APP_ENV=production
ENV SECRET_KEY=
ENV DATABASE_URI=

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysqlclient

COPY . .

EXPOSE 80/tcp
EXPOSE 443/tcp
