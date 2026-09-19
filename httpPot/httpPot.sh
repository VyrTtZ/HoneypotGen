#!/bin/bash

socat -dd -lf httpPot.log TCP-LISTEN:1234,fork,reuseaddr EXEC:./controller.sh