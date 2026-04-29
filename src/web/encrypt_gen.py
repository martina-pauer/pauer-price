#!/usr/bin/python3
# Set a New Encryption modificating JSON values in file
def get_input_keys() -> dict[str, str]:
    '''
        Get dictionary of file
    '''
    json_input = open('encrypt.json', 'r')
    
    text: str = ''

    for line in json_input.readlines():
        text += line                
    import json

    return json.loads(text)

def random_unicode() -> str:
    '''
        Generate Random Unicode
        Codes Web Safe
    '''
    code = '\\u'

    import random
    
    # Generate codes from U+0021 to U+007E for printable character
    code += f'00{hex(random.randint(2, 7)).replace('0x', '').upper()}{hex(random.randint(1, 14)).replace('0x', '').upper()}'
        
    return code
    
def change_values() -> dict[str, str]:
    '''
        Give dictionary with new randoms values
        for each key changing unicode code to
        other different to alls
    '''
    codes_for_inputs: dict[str, str] = get_input_keys()
    
    for input_key in codes_for_inputs.keys():
        unicode_code: str = random_unicode()
        while (codes_for_inputs.__contains__(unicode_code)):
            # Repeat Proces for generate random unicode_code
            unicode_code: str = random_unicode()
        # When is different to all codes in dict change    
        codes_for_inputs[input_key] = unicode_code
    # This Algorithm give all different codes between them and different to before 
    return codes_for_inputs
# Change and write to file new values
new_unicode: dict[str, str] = change_values()
encryption = open('encrypt.json', 'w')
# Write in JSON encryption file
encryption.write('{\n')
ending: str = ','
for relation in new_unicode.keys():
    # When Is last Key don't add comma in the end
    if relation == ' ':
        ending = ''
    # Write values as JSON line
    encryption.write(f'\t"{relation}": "{new_unicode[relation]}"{ending}\n')    
del new_unicode, ending
encryption.write('}')
encryption.close()
del encryption
print('\n\t[New Encryption loaded to "encrypt.json"]\n\t')