from twilio.rest import Client

account_sid = 'AC32518db309c306c0e759b077ed21b260'
auth_token = '2aead7154e0fd1198af7ca3fc8cfbbb8'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body='Olá! Esta é uma mensagem de teste via Twilio.',
    to='+5535999195960',
    from_='+15304646743'
)

print(message.sid)
