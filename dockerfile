FROM python:3.10

WORKDIR /app  
# Set the working directory

COPY . .  
# Copy all files from current directory to container

RUN pip install --no-cache-dir -r requirements.txt 
 # Install dependencies

EXPOSE 5000
CMD ["python", "place.py"]  
# Run the application
