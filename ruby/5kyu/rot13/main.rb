def rot13(message)
  alphabet = [*'a'..'z', *'a'..'z', *'A'..'Z', *'A'..'Z']
  new_message = []
  message.chars.each do |element|
    if alphabet.include?(element)
      index = alphabet.find_index(element)
      new_message << alphabet[index + 13]
    else
      new_message << element
    end
  end
  new_message.join
end

#BEST practice
# def rot13(message)
#   p message.tr('a-zA-Z', 'n-za-mN-ZA-M')
# end
