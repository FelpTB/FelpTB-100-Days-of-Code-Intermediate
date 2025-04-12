from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client('AC32518db309c306c0e759b077ed21b260','2aead7154e0fd1198af7ca3fc8cfbbb8')

    def send_sms(self, message_body):

        message = self.client.messages.create(
            from_='+15304646743',
            body=message_body,
            to='+5535999195960'
        )
        # Prints if successfully sent.
        print(message.sid)
