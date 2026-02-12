FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for caching
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn for Flask
RUN pip install gunicorn

# Copy application code
COPY api/ ./api/

# Create the notebooks/models directory structure
RUN mkdir -p /app/notebooks/models

# Copy model files to the EXACT path your code expects
COPY notebooks/models/rf_sm_fraud.pkl /app/notebooks/models/
COPY notebooks/models/feature_names.json /app/notebooks/models/
COPY notebooks/models/preprocessing_info.json /app/notebooks/models/

# Set Python path
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Expose port
EXPOSE 8000

# Run Flask with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "api.app:app"]