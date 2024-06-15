FROM python:3.11

WORKDIR /shopping_tickets
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

WORKDIR /shopping_tickets
RUN ls
RUN python manage.py makemigrations
RUN python manage.py migrate

VOLUME ["/shopping_tickets/data"]
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=shopping_tickets.settings.production
ENV SECRET_KEY=ep=*gxn9xwb@v!owzlo+8-g8_c3860v98043u5^!pw)0pyd(&^
ENV ALLOWED_HOSTS=".localhost, .zeppelin.dev, *"
ENV DEBUG=False

ENV PYTHONUNBUFFERED 1
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "--chdir", "shopping_tickets", "--bind", "0.0.0.0:8000", "shopping_tickets.wsgi:application"]
