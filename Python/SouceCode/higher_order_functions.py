def shout(message):
    return message.upper()

def whisper(message):
    return message.lower()


def greet(function):
    greeting_message = function("Hello, Have A Nice Day...!")
    print(greeting_message)


greet(shout)
greet(whisper)
