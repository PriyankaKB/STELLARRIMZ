from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="myapp/static"), name="static")

# Allow requests from anywhere (for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000", "https://stellarrimz.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_data():
    return {
        "message": "Hello from Stell-E!",
        "image_url": "/static/Stell-E.png"
    }
