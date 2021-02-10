
def count_replies(messages):
    replies = {}
    for message in messages:
        print(message)
        if 'replies' in message and message['replies'] and message['replies']['replies'] > 2:
            id = message['id']
            reply = message['replies']
            replies[id] = reply['replies']
    return replies