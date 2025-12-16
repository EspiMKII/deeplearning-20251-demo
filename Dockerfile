FROM python:3.10.19-slim
WORKDIR /app

RUN apt-get update && apt-get upgrade
RUN apt-get install -y --no-install-recommends build-essential

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# tells container to listen on this port
EXPOSE 5000

# Remember, CMD uses a list form, with the command arguments
CMD # [something here]
