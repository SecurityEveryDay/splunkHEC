import requests
import json

# Define the HEC function, which sends events to Splunk
def HEC(token, url, index, sourcetype, event):
        # Define the headers of the HTTP request
        headers = {
                'Authorization': 'Splunk '+token+'', # Add authorization token
                'Content-Type': 'application/x-www-form-urlencoded', # Set content type as "application/x-www-form-urlencoded"
                }

        # Define the parameters of the HTTP request
        params = {
                'channel': token, # Add token as parameter of the request
                }

        # Define the data to be sent in the body of the HTTP request
        data = {
                'event': event, # Add the event
                'index': index, # Add the index
                'sourcetype': sourcetype, # Add the source type
        }

        # Convert the data into a string in JSON format
        data = json.dumps(data)

        # Send the HTTP request to the Splunk HTTP Event Collector (HEC)
        hec = requests.post(url, params=params, headers=headers, data=data, verify=False)

        # Check if the request status is equal to 200 (success)
        if hec.status_code == 200:
            # Print the result of the request
            print(hec.text)
        else:
            # While the request status is different from 200, resend the request
            while hec.status_code != 200:
                hec = requests.post(url, params=params, headers=headers, data=data)

        # Print the result of the request
        print(hec.text)
