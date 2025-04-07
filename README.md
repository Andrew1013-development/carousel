# Carousel
## Features
## Installation
### Docker Compose (recommended)
```yaml
services:
  carousel:
    container_name: carousel
    image: andrew1013/carousel:latest
    ports:
      - 5000:5000
    volumes:
      - ./path/to/images:/images
      - ./path/to/config.json:/app/config.json
    environment:
      TZ: Asia/Ho_Chi_Minh # modify this to your time zone
    labels:
      glance.name: Carousel # Container name as it appears in Glance Dashboard
    restart: unless-stopped
```
## Configuration (recently added in v0.2.4)
## Building and Developing
Dockerfile
```dockerfile
FROM python:3.13.1

WORKDIR /app
COPY /app/blueprints/ blueprints/
COPY /app/__init__.py __init__.py
COPY /requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", ".", "run", "--host", "0.0.0.0"]
```