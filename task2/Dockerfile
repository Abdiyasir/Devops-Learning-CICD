FROM python:3.8-slim
WORKDIR /project
COPY . /project
RUN pip install flask redis
EXPOSE 5001
CMD ["python", "app.py"]
