# my first solution
def alphabet_position(text):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  text_to_change = list(text.lower())

  new_array = []
  for n in text_to_change:
    if n in alphabet:
      index = alphabet.index(n)
      new_array.append(index+1)
  return " ".join(map(str, new_array))


# better solution
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
