"""
PURPOSE: Collection of common functions.
"""

import os, json
from googleapiclient.discovery import build
from dotenv import load_dotenv
from google.oauth2.credentials import Credentials



# Gets specific .env variable.
def get_env(env_var):
    load_dotenv("Credentials/.env")
    return(os.getenv(env_var))


# Prints to .json file.
def print_to_file(input, file_name):
    file_directory = "Output/" + file_name
    
    if type(input) == list:
        vid_dict = [video.__dict__ for video in input]
        with open(file_directory, "w") as f:
            json.dump(vid_dict, f)
    else:
        with open(file_directory, "w") as f:
            json.dump(input, f)


# Builds YT Data API service obj.
def build_service_obj(api_key):
    api_service_name = "youtube"
    api_version = "v3"


    """
    if-else statement that builds youtube obj. based on api_key's obj. type.
    """
    if isinstance(api_key, Credentials):
        youtube = build(api_service_name, api_version, credentials=api_key)
    else:
        youtube = build(api_service_name, api_version, developerKey=api_key)

    
    return youtube