# Dictionary mapping characters to their Braille representation
BRAILLE_MAP = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
    'z': '⠵',
    '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙',
    '5': '⠼⠑', '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓',
    '9': '⠼⠊', '0': '⠼⠚',
    ' ': '⠀',
}

def text_to_braille(text):
    braille = ''
    for char in text.lower():
        if char in BRAILLE_MAP:
            braille += BRAILLE_MAP[char]
        else:
            braille += char  # If the character is not in the map, keep it unchanged
    return braille

# Example usage
text = "Hello World!"
braille_text = text_to_braille(text)
print(braille_text)



'''
chatbot

- braille
- voice

'''