from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC55573c540fefe3da57c064bbf232d061"
auth_token  = "{{ 451ec3e2da8ae9a167a5fbc3ce3bfafc }}"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi Luiz?! Where are you?",
    to="+556181654530",    # Replace with your phone number
    from_="+555140421687") # Replace with your Twilio number
print message.sid

