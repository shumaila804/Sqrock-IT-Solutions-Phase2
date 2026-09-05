FROM python:latest
EXPOSE 22
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]