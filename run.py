# run.py

import os
from app import app

app.run(host = os.getenv('IP', '127.0.0.1'), port = int(os.getenv('PORT', 5000)))