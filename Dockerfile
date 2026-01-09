FROM python:3.13.11-slim
WORKDIR /work

RUN apt-get update && apt-get upgrade
# these libraries are here because apparently openCV is just cringe
RUN apt-get install -y --no-install-recommends build-essential ffmpeg libsm6 libxext6

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# tells container to listen on this port
EXPOSE 5000

COPY app/ app/

# Remember, CMD uses a list form, with the command arguments
CMD ["python3", "app/src/base.py"]
