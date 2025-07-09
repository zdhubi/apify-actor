FROM python:3.9-slim

WORKDIR /app

# 📦 Instalace Firefoxu a Geckodriveru
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# ⚙️ Instalace Geckodriveru
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz && \
    tar -xvzf geckodriver-v0.34.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.34.0-linux64.tar.gz

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]

