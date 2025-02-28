FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "5000"]

# ✅ Allows containerized inference API
# ✅ Ensures environment consistency