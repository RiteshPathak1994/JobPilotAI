from fastapi import FastAPI

app = FastAPI(
    title = "JobPilot AI",
    description = "Autonomous AI Career Copilot",
    version= "0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to JobPilot AI"
    }
