def count_replies(messages):
    replies = {}
    forwards = {}
    for message in messages:
        print(message)
        if 'replies' in message and message['replies'] and message['replies']['replies'] > 2:
            id = message['id']
            reply = message['replies']
            replies[id] = reply['replies']
        if 'forwards' in message and message['forwards']:
            id = message['id']
            forwards[id] = message['forwards']
    return replies, forwards

