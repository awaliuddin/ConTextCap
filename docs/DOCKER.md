# Docker Guide for ConTextCap

This guide explains how to run ConTextCap using Docker.

## Quick Start

### Using Docker

```bash
# Build the image
docker build -t contextcap:latest .

# Run ConTextCap
docker run -v $(pwd)/projects:/data/projects:ro \
           -v $(pwd)/output:/data/output \
           contextcap:latest
```

### Using Docker Compose

```bash
# Build and run
docker-compose up contextcap

# Run in background
docker-compose up -d contextcap

# View logs
docker-compose logs -f contextcap

# Stop
docker-compose down
```

## Configuration

### Environment Variables

- `DISPLAY`: X11 display for GUI (default: `:99`)
- `QT_QPA_PLATFORM`: Qt platform (default: `offscreen`)
- `PYTHONUNBUFFERED`: Python output buffering (default: `1`)

### Volume Mounts

- `/data/projects`: Mount your source code here (read-only)
- `/data/output`: Mount output directory here
- `/app/config`: Optional configuration directory

## Development Mode

For development with hot-reload:

```bash
docker-compose --profile dev up contextcap-dev
```

## GUI Support

### Linux (X11)

```bash
# Allow Docker to connect to X server
xhost +local:docker

# Run with GUI
docker run -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
           -v $HOME/.Xauthority:/root/.Xauthority:ro \
           --network host \
           contextcap:latest
```

### macOS (XQuartz)

```bash
# Install XQuartz
brew install --cask xquartz

# Start XQuartz and enable network connections
# XQuartz > Preferences > Security > "Allow connections from network clients"

# Get your IP
IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')

# Allow X11 forwarding
xhost + $IP

# Run with GUI
docker run -e DISPLAY=$IP:0 \
           -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
           contextcap:latest
```

### Windows (VcXsrv)

```powershell
# Install VcXsrv
# Download from https://sourceforge.net/projects/vcxsrv/

# Start VcXsrv with "Disable access control" checked

# Run with GUI
docker run -e DISPLAY=host.docker.internal:0 \
           contextcap:latest
```

## Headless Mode

For PDF generation without GUI:

```bash
docker run -e QT_QPA_PLATFORM=offscreen \
           -v $(pwd)/projects:/data/projects:ro \
           -v $(pwd)/output:/data/output \
           contextcap:latest
```

## Advanced Usage

### Custom Dockerfile

Create a custom Dockerfile for specific needs:

```dockerfile
FROM contextcap:latest

# Install additional tools
USER root
RUN apt-get update && apt-get install -y git
USER contextcap

# Add custom configuration
COPY --chown=contextcap:contextcap custom-config.yml /app/config/
```

### Resource Limits

```bash
docker run --cpus="2.0" \
           --memory="2g" \
           -v $(pwd)/projects:/data/projects:ro \
           -v $(pwd)/output:/data/output \
           contextcap:latest
```

### Multi-platform Build

```bash
# Build for multiple platforms
docker buildx build --platform linux/amd64,linux/arm64 \
                    -t contextcap:latest \
                    --push .
```

## Troubleshooting

### Qt Platform Plugin Error

If you see "qt.qpa.plugin: Could not find the Qt platform plugin":

```bash
# Use offscreen mode
docker run -e QT_QPA_PLATFORM=offscreen contextcap:latest
```

### Permission Issues

If you encounter permission issues with volumes:

```bash
# Run with your user ID
docker run --user $(id -u):$(id -g) \
           -v $(pwd)/output:/data/output \
           contextcap:latest
```

### Display Issues

If GUI doesn't work:

```bash
# Check X11 connection
docker run -e DISPLAY=$DISPLAY \
           -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
           --rm -it contextcap:latest \
           xeyes
```

## Best Practices

1. **Use volumes** for input/output, not COPY in Dockerfile
2. **Run as non-root** (already configured)
3. **Set resource limits** for production
4. **Use offscreen mode** for CI/CD
5. **Cache layers** by copying requirements first

## CI/CD Integration

### GitHub Actions

```yaml
- name: Build Docker image
  run: docker build -t contextcap:latest .

- name: Run tests in Docker
  run: docker run contextcap:latest pytest
```

### GitLab CI

```yaml
test:
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t contextcap:latest .
    - docker run contextcap:latest pytest
```

## Examples

### Batch Processing

```bash
# Process multiple projects
for project in projects/*; do
  docker run -v $project:/data/project:ro \
             -v $(pwd)/output:/data/output \
             contextcap:latest \
             python ConTextCap.py --input /data/project
done
```

### Automated Pipeline

```bash
#!/bin/bash
# Generate PDFs from git repositories

REPOS=("user/repo1" "user/repo2")

for repo in "${REPOS[@]}"; do
  git clone https://github.com/$repo temp_repo

  docker run -v $(pwd)/temp_repo:/data/project:ro \
             -v $(pwd)/output:/data/output \
             contextcap:latest

  rm -rf temp_repo
done
```

---

For more information, see the [main documentation](README.md).
