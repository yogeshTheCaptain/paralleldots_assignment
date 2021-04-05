# get python
FROM python:3.8.3-buster 

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# Copy only requirements to cache them in docker layer
WORKDIR /code

# install necessary libraries
RUN pip3 install celery
RUN pip3 install fastapi
RUN pip3 install uvicorn

# Creating folders, and files for a project:
COPY app.py /code/app.py
COPY worker.py /code/worker.py
