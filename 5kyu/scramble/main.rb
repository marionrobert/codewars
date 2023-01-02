def scramble(s1,s2)
  s2.chars.all? { |letter| s2.count(letter) <= s1.count(letter) }
end
# comment
