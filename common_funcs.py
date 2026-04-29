"""
PURPOSE: Collection of common functions.
"""

import os, json
from dotenv import load_dotenv
from Classes.Video import Video




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