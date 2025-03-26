# Use the official MkDocs Material image
FROM squidfunk/mkdocs-material:latest

# Set the working directory
WORKDIR /docs

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy MkDocs files
COPY mkdocs.yml .

# Copy in docs
COPY docs docs

# Expose the MkDocs server port
EXPOSE 8000