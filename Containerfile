FROM python:3.11

RUN pip install pytz

COPY main.py /app/

CMD python3 /app/main.py
