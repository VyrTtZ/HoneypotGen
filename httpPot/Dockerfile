FROM bash:4.4

WORKDIR /app

RUN apk add --no-cache socat

COPY controller.sh httpPot.sh index.html ./

RUN chmod +x controller.sh httpPot.sh

EXPOSE 80

CMD ["bash", "httpPot.sh"]