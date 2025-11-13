FROM python:3.12-alpine

#creating the workdir for container
WORKDIR /usr/local/app

# Copy only requirements first for better layer caching
COPY ./model_res/requirement.txt ./requirements.txt

# Install build deps needed for many wheels
RUN apk add --no-cache build-base libffi-dev openssl-dev musl-dev python3-dev

# Upgrade pip and install python deps
RUN pip install --upgrade pip \
 && pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy app code
COPY . .

# Create non-root user, fix ownership, and switch
RUN adduser -D app && chown -R app:app /usr/local/app
USER app

EXPOSE 8501

# Run Streamlit and bind to localhost only
CMD ["streamlit", "run", "streamlit.py", "--server.address=0.0.0.0", "--server.port=8501"]

