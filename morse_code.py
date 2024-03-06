from codes_list import codes

def generateMorseCode(sentence: str) -> str:
    '''
    function returns a morse code generated for the given argument
    '''

    morse_code = ""

    for letter in sentence:
        if letter >= 'a' and letter <= 'z':
            morse_code += codes[letter.upper()]
        else:
            morse_code += codes[letter]
        morse_code += " "
    
    return morse_code