FROM fedora:latest

RUN dnf update -y && dnf install -y python3 python3-paramiko
WORKDIR /app
COPY sshPot.py .
EXPOSE 22
CMD ["python3", "sshPot.py"]




