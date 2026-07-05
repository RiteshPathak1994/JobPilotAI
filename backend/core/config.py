from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "JobPilot AI")
    APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

settings = Settings()