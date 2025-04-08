# Carousel
## Features
## Installation
### Step 0: Glance Dashboard
**Disclaimer: Glance must be installed and up-and-running before proceeding to install this widget.**

Their official installation instructions can be found [here](https://github.com/glanceapp/glance/blob/main/README.md#installation), you are highly advised to follow this guide before you go on to this.
### Step 1: Folder structures
You should have these files and folders in the directory you plan to install Carousel in:
- Image folder, contained in separate folders with their respective names
- Configuration file `config.json`
- (optional) Logs folder (Carousel will write logs to this folders)
### Step 2: Configuration
Paste the provided template below into your `config.json`:
```json
{
    "IMG_DIR": "", // image directory as noted from step 1
    "LOG_DIR": "", // logs directory as noted from step 1
    "MODE": 2
}
```
Populate the required fields as laid out by the comments.

More information is available on these settings in [Configuration](#configuration-wip---v024).
### Step 3: Docker Compose (recommended)
_Note: As mentioned in Step 0, this guide will not include instructions on setting up Glance Dashboard in Docker. If you have made it this far without reading the disclaimer, you may follow their [installation instructions](https://github.com/glanceapp/glance/blob/main/README.md#installation) before continuing on this part._

Paste this into your `docker-compose.yml` file, under the top-level property `services`:
```yaml
carousel:
  container_name: carousel
  image: andrew1013/carousel:latest
  ports:
    - 5000:5000
  volumes:
    - ./path/to/images:/images # Directory to your image folder
    - ./path/to/config.json:/app/config.json # Directory to your config.json
    - ./path/to/logs:/logs # Directory to your logs folder
  environment:
    TZ: Asia/Ho_Chi_Minh # Modify this to your time zone
  labels:
    glance.name: Carousel # Container name as it appears in Glance Dashboard
  restart: unless-stopped
```
Modify any values deemed necessary as laid out in the comments.
### Step 4: Widget Setup
```yaml
- type: custom-api
  title: Image Carousel (Experimental)
  url: https://localhost:5000/carousel
  allow-insecure: true
  parameters:
    count: 10
  cache: 10s
  template: |
    {{ if .JSON.Exists "error" }}
    <div class="widget-error-header">
      <p class="size-h2 color-negative">{{ .JSON.String "error" }}</p>
      <svg class="widget-error-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z"></path>
      </svg>
    </div>
    <p class="size-h4">{{ .JSON.String "resolution" }}</p>
    {{ else }}
    <div class="cards-grid">
      {{ range .JSON.Array "images"}}
      <div class="card">
        <p class="size-h2 color-primary">{{ .String "name" }}</p>
        <img src={{ .String "url" }} style="border-radius: 10px; " loading="lazy">
      </div>
      {{ end }}
    </div>              
    <hr class="margin-block-15">
    <p class="color-highlight">Last updated on {{ .JSON.String "requested" }}</p>
    <p class="color-highlight">Version {{ .JSON.String "version"}}</p>
    {{ end }}
```
## Configuration (WIP - v0.2.4)
Configuration is saved in `config.json`

Available settings:
- `IMG_DIR`: Image directory (absolute or relative path)
- `LOG_DIR`: Logs directory (absolute or relative path)
- `DEBUG`: Toggle debug mode (defaults to false)
- `MODE`: Picking algorithm (1 - sequential or 2 - randomized) 
## Building from source
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
## Contributing guidelines
## Thank you