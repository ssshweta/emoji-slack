#!/usr/bin/env python3
import sys
import json
import random

def getEmojifiedVersion(message):
    with open('./translator.json') as t_file:
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
    with open('./emoji-list.json') as t_file:
        replacements = json.load(t_file)
        newMessage = message.lower()

        for alias in replacements['aliases'].keys():
            newMessage = newMessage.replace(alias, replacements['aliases'][alias])

        for replacement in replacements['pure']:
            newMessage = newMessage.replace(replacement, ":{}:".format(replacement))
        
        return newMessage

if __name__ == "__main__":
    originalMessage = input("Enter message: ")
    print("\nEmoji String:")
    print(getEmojifiedVersion(originalMessage))

    print("\nEmoji-word Replacement Strings:")
    print(pepperWithEmojis(originalMessage))

