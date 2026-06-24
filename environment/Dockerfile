# python:3.12-slim pinned by digest for reproducibility
FROM python:3.12-slim@sha256:adc05bebf0ded87b863e91f7d0e399d821f68b1a5a8eabaed2acfa90763be768

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

# Only copy the task data — solution files must NOT be in the agent image
COPY access.log /app/access.log
