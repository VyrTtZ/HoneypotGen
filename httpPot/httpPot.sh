#!/bin/bash
socat -dd -v TCP-LISTEN:80,fork,reuseaddr SYSTEM:"bash controller.sh"
