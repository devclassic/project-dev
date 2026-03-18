import multiprocessing

multiprocessing.freeze_support()

import uvicorn
from app import app

uvicorn.run(app, host="0.0.0.0", port=8000)
