FROM python:3.12-slim


WORKDIR /app


RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    x11vnc \
    novnc \
    websockify \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


COPY entrypoint.sh .


RUN chmod +x entrypoint.sh


EXPOSE 6080


CMD ["./entrypoint.sh"]