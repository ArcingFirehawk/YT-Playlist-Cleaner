"""
PURPOSE: Collection of common functions.
"""

import os
from dotenv import load_dotenv


def get_env(env_var):
    load_dotenv("Credentials/.env")
    return(os.getenv(env_var))