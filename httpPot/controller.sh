#!/bin/bash;
first=""
isPost=0

while read -r header; do
        header="${header%$'\r'}"

        if [[ -z "$first" ]]; then
                first="$header"
                [[ "$first" == POST* ]] && isPost=1
        fi

        [[ -z "$header" ]] && break
done

if [[ "$isPost" -eq 1 ]]; then
        read -r -t 1 body
        body="${body%$'\r'}"
        timestamp="$(date '+%Y-%m-%d %H:%M:%S')"
        echo "[$timestamp] ip: $SOCAT_PEERADDR - data: $body" >> httpPot.log

fi


printf 'HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: text/html\r\nContent-Length: 366\r\n\r\n'
cat index.html