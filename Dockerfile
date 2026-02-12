FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for caching
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# EXPLICITLY INSTALL UVICORN
RUN pip install gunicorn

# Copy application code
COPY api/ ./api/
COPY models/ ./models/

# Set Python path
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Expose port
EXPOSE 8000

# Run Flask with gunicorn (WSGI)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "api.app:app"] 