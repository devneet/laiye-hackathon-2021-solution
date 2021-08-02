
def getticketclassification(endpointurl, emailbody):
    import requests

    dict_Output = {}

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Do the HTTP request
    response = requests.get(endpointurl+emailbody, headers=headers)

    # Check for HTTP codes other than 200
    if response.status_code != 200 | response.status_code != 201:
        raise Exception("Status: "+str(response.status_code)+", Headers: "+str(response.headers)+", Error Response: "+response.json())

    # Decode the JSON response into a dictionary and use the data
    data = response.json()

    dict_Output[(data['prediction']['topIntent'])] = round((data['prediction']['intents'][(data['prediction']['topIntent'])]['score']),2)
    return dict_Output