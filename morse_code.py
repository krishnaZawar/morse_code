from codes_list import codes, keys

def generateMorseCode(sentence: str) -> str:
    '''
    function returns a morse code generated for the given sentence
    '''

    morse_code = ""

    for letter in sentence:
        if letter >= 'a' and letter <= 'z':
            morse_code += codes[keys.index(letter.upper())]
        elif not letter in keys:
            continue
        else:
            morse_code += codes[keys.index(letter)]
        morse_code += " "
    
    return morse_code.strip()

def decodeMorseCode(encoded_msg: str) -> str:
    '''
    function decodes a given morse code
    '''
    msg = ""
    individual_code = ""
    for code_bit in encoded_msg:
        if code_bit == ' ':
            if individual_code in codes:
                msg += keys[codes.index(individual_code)]
                individual_code = ""
            else:
                return "morse code is incorrect"
            continue
        else:
            individual_code += code_bit
    if individual_code not in codes:
        return "morse code is incorrect"
    msg += keys[codes.index(individual_code)]
    return msg