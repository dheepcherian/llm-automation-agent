# Use official Python image as base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the current project files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Command to start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
 
