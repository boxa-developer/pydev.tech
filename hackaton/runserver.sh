#!/bin/bash
echo "[pydev.tech] server is started"
source .venv/bin/activate
python3 manage.py runserver 0.0.0.0:80
echo "[pydev.tech] server is closing"