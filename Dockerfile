FROM python:3.10-slim-buster

# Set the working directory in the Docker image
WORKDIR /task_Manager

# Copy the requirements file and install dependencies
COPY ./requirements.txt /requirements.txt
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \ 
    libjpeg62-turbo-dev \ 
    zlib1g-dev \ 
    libwebp-dev \
    netcat \
 && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip 
RUN pip install -r /requirements.txt

# Create necessary directories and copy the project files
RUN mkdir /task_Manager/media
COPY ./ /task_Manager

# Make the script executable
COPY entrypoint.sh /task_Manager/
RUN chmod +x /task_Manager/entrypoint.sh


# Run the script as the default command
CMD [ "/task_Manager/entrypoint.sh" ]

