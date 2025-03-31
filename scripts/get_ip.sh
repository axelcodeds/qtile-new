#!/bin/bash
IP=$(ip -4 addr show enp0s3 | grep -oP '(?<=inet\s)\d+(\.\d+){3}' || echo "Sin IP")
echo "  $IP"