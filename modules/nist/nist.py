import requests
import time
#import logger
import json

nvd_sources = [
    "https://services.nvd.nist.gov/rest/json/cves/2.0"
]


WEBHOOK_URL = "" 
MESSAGE_USERNAME = "CVETICKER"        #username that will be displayed when the embeded message is output into the channel



def send_discord_message(title:str, link:str, date:str, description:str) -> None:
    

    data = {
    "content" : "",
    "username" : MESSAGE_USERNAME
    }

    data["embeds"] = [
        {
            "description" : link + "\n" + description + "\n" + date,
            "title" : title
        }
    ]

    send_request = requests.post(WEBHOOK_URL, json=data)

    try:
        send_request.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        #log_error(err)
    else:
        #log_info("Webhook used successfully, code {}.".format(send_request.status_code))
        print("Webhook used successfully, code {}.".format(send_request.status_code))




def check_db(url:str) -> bool:
    pass

def populate_db(data) -> None:
    with open("database_file.json", "w") as write_file:
        json.dump(data, write_file)

 
def load_db():
    with open("database_file.json", "r") as read_file:
        return json.loads(read_file)

def query_nist():
    url = 'https://services.nvd.nist.gov/rest/json/cves/2.0/'


    params = {
        'pubStartDate': '2023-01-03T00:00:00.000-05:00',
        'pubEndDate': '2023-01-04T23:59:59.999-05:00'
    }


    try:
        response = requests.get(url, params=params)

    except response.status_code != 200:
        print(f"Error: {response.status_code}")
        
    else:
        return response.json()

        





if __name__ == "__main__":
    query_data = query_nist()
    populate_db(query_data)
    db_data = load_db()
    print(db_data)
    #for cve in db_data['cve']:
     #   print(cve)



    
