# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /

# Copy the requirements file into the container
COPY requirements.txt .

# Install system dependencies
# RUN apt-get update && \
#   apt-get install -y --no-install-recommends \
#   build-essential \
#   pango1.0-0 \
#   pkg-config \
#   libffi-dev \
#   libpango1.0-dev \
#   libgirepository1.0-dev \
#   libcairo2-dev \
#   gir1.2-pango-1.0 \
#   libgirepository1.0-dev \
#   && rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y libcairo2-dev pkg-config python3-dev
RUN apt-get install -y libsdl-pango-dev
RUN apt-get install -y ffmpeg
# RUN apt-get install -y pango
RUN apt-get install -y libpango1.0-0
# RUN apt-get install -y scipy
RUN apt-get install -y python3-scipy

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variables
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Run the application
CMD ["python", "manim_test.py"]
