#!/usr/bin/env python3
import sys
import json
import random

def getEmojifiedVersion(message):
    with open('/Users/dlopez7/dev/emoji-slack/translator.json') as t_file:
        translator = json.load(t_file)
        newMessage = ''

        for letter in message:
            if letter.lower() in translator:
                options = translator[letter.lower()]
                newMessage += random.choice(options)
            else:
                newMessage += letter
        
        return newMessage

def pepperWithEmojis(message):
    with open('/Users/dlopez7/dev/emoji-slack/emoji-list.json') as t_file:
        replacements = json.load(t_file)
        newMessage = message.lower()

        for replacement in replacements:
            newMessage = newMessage.replace(replacement, ":{}:".format(replacement))
        
        return newMessage

if __name__ == "__main__":
    originalMessage = input("Enter message: ")
    print(getEmojifiedVersion(originalMessage))
    print(pepperWithEmojis(originalMessage))

