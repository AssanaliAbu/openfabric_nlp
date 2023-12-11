# Use the latest openfabric/tee-python-cpu image as the base image
FROM openfabric/tee-python-cpu:latest

# Create a new directory called 'application' in the container's filesystem
RUN mkdir application

# Set the 'application' directory as the working directory for subsequent instructions
WORKDIR /application

# Copy all files from the current directory on the host to the current working directory in the container
COPY . .

# Install PyTorch, torchvision, and torchaudio from the specified PyTorch wheel index (for CUDA 11.8)
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install the Wikipedia-API library using pip
RUN pip install Wikipedia-API

# Install the transformers library using pip
RUN pip install transformers

# Install the application's Python dependencies using Poetry without installing the dev dependencies
RUN poetry install -vvv --no-dev

# Inform Docker that the container listens on port 5500 at runtime
EXPOSE 5500

# Set the command to be executed when the container starts, which is to run the 'start.sh' shell script
CMD ["sh","start.sh"]
