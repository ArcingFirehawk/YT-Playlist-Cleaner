"""Testing how to read variables from a .env file."""

from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("API_KEY"))