#!/bin/bash
socat -dd -v TCP-LISTEN:1234,fork,reuseaddr EXEC:./controller.sh