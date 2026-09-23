#!/bin/bash
socat -dd -v TCP-LISTEN:80,fork,reuseaddr EXEC:./controller.sh