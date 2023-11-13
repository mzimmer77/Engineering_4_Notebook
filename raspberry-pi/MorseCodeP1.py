#type: ignore
#imports
import time 

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}
    # this is the mosrse code library

while True: 
    #lowercases letters
    message = input("Your Message: ").upper()
    #defines message
    tmessage = ""
    #exits code if "-q" is tpyed
    if "-Q" in message: #loop with message
        break
    
    for letter in range(len(message)): #converts # to letters
       
        tmessage += MORSE_CODE[message[letter]] + " "
    #prints message
    print(f"Your Translation: {tmessage}")
    time.sleep(1)