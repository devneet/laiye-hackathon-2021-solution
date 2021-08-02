from twilio.rest import Client

def make_call(account_sid,auth_token,to_number,from_number, call_context) :


    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            twiml='<Response><Say>{0}</Say></Response>'.format(call_context),
                            to= to_number,
                            from_= from_number
                        )
