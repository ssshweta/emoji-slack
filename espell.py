#!/usr/bin/env python3

import json
import random


with open('translator.json') as t_file:
    translator = json.load(t_file)

    originalMessage = input("Input: ")
    newMessage = ''
    
    for letter in originalMessage:
        if letter.lower() in translator:
            options = translator[letter.lower()]
            newMessage += random.choice(options)
        else:
            newMessage += letter
    
    print(newMessage)
