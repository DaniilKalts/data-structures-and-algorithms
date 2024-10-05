# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install pytest-tui to run tests
RUN pip install pytest-tui

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Default command to run tests using pytest with color enabled
CMD ["pytest", "--tui", "--color=yes"]
