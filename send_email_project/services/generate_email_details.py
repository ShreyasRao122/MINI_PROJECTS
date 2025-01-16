import json
def generate_email_details(file_path):
    with open(file_path,"r") as file:
        data=json.loads(file.read())
    return data



