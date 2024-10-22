# cors.py
from fastapi.middleware.cors import CORSMiddleware

def add_cors(app):
    # Define allowed origins
    origins = [
        "http://0.0.0.0:80",  # your frontend app URL
    ]

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # Allows specific origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods
        allow_headers=["*"],  # Allows all headers
    )
