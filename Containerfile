FROM python:3.11

RUN pip install pytz

COPY main.py /app/

ENTRYPOINT ["python3", "/app/main.py"]
