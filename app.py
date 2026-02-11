from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import os
import logging
from datetime import datetime
import socket

app = FastAPI()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Read environment variables with defaults
PORT = os.environ.get('PORT', '8080')
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'unknown')
VERSION = os.environ.get('VERSION', 'unknown')


def get_hostname():
    """Get the hostname of the current system"""
    try:
        return socket.gethostname()
    except Exception:
        return 'unknown'


@app.get('/', response_class=HTMLResponse)
def home():
    """Main page endpoint"""
    timestamp = datetime.now().isoformat()
    hostname = get_hostname()

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Hello World - {ENVIRONMENT}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .container {{ max-width: 600px; margin: 0 auto; }}
        .info {{ background: #f0f0f0; padding: 20px; border-radius: 5px; }}
        h1 {{ color: #333; }}
        .env {{ color: #0066cc; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello World FastAPI!</h1>
        <div class="info">
            <p><strong>Environment:</strong> <span class="env">{ENVIRONMENT}</span></p>
            <p><strong>Version:</strong> {VERSION}</p>
            <p><strong>Timestamp:</strong> {timestamp}</p>
            <p><strong>Hostname:</strong> {hostname}</p>
        </div>
    </div>
</body>
</html>
    """


@app.get('/health')
def health():
    """Health check endpoint"""
    return JSONResponse(
        content={
            'status': 'healthy',
            'environment': ENVIRONMENT,
            'version': VERSION
        },
        status_code=200
    )


@app.get('/ready')
def ready():
    """Readiness check endpoint"""
    return JSONResponse(
        content={
            'status': 'ready',
            'environment': ENVIRONMENT,
            'version': VERSION
        },
        status_code=200
    )


if __name__ == '__main__':
    import uvicorn
    port = int(PORT)
    logger.info(f'Starting Hello World Python FastAPI server on port {port}')
    logger.info(f'Environment: {ENVIRONMENT}')
    logger.info(f'Version: {VERSION}')
    uvicorn.run(app, host='0.0.0.0', port=port)
