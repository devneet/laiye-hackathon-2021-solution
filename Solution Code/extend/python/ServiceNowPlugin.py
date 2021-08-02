def create_incident(instance_name, username, password, category, short_text, description):
    import requests

    # Set the request parameters
    url = "https://"+instance_name+".service-now.com/api/now/table/incident"

    user = username
    pwd = password

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    payload = '{"comments":"'+description+'","short_description":"'+short_text+'","category":"'+category+'"}'

    # Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers, data=payload)

    # Check for HTTP codes other than 200
    if response.status_code != 200 | response.status_code != 201:
        raise Exception("Status: "+str(response.status_code)+", Headers: "+str(response.headers)+", Error Response: "+response.json())

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    return data['result']['number']
