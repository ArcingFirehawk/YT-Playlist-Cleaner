"""
PURPOSE: Collection of common functions.
"""

import os, json
import googleapiclient.discovery
from dotenv import load_dotenv



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
def build_service_obj(need_auth, api_key):
    api_service_name = "youtube"
    api_version = "v3"


    """
    if-else statement to test if need_auth is True or False to determine type of obj. to build.
    True creates authorized service obj., False creates simple service obj.
    """
    if need_auth:
        youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=api_key)
    elif not need_auth:
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
    else:
        youtube = None
    
    return youtube