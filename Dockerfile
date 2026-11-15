# Use a lightweight official Python runtime
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies first (this leverages Docker layer caching 
# so you don't reinstall packages every time you change your code)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .


EXPOSE 8000

# Command to run the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]