FROM python:3.12-slim

WORKDIR /app

RUN pip install paramiko

COPY sshPot.py .

EXPOSE 22

CMD ["python", "sshPot.py"]