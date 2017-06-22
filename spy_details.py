from datetime import datetime
#Details of existed user
spy={
    'name':"Rumi",
    'salutation':'Mr.',
    'age':21,
    'rating':0.0
}

friends = [
    {
        'name': 'Nikola Tesla',
        'salutation': 'Dr.',
        'rating': 4.9,
        'age': 27,
        'chats': []
    },
    {
        'name': 'Che Guevara',
        'salutation': 'Dr.',
        'rating': 4.95,
        'age': 21,
        'chats': []
    }
]

class chatmessage:
    def __init__(self,message,sent_by_me):
        self.message=message
        self.time=datetime.now()
        self.sent_by_me=sent_by_me
