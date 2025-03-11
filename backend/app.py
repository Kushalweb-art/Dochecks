from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import validation, upload, databases

app = FastAPI()

# CORS settings to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(validation.router)
app.include_router(upload.router)
app.include_router(databases.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Data Validation API"}
