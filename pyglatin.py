print 'Pig Latin begins!'

name = raw_input('Whats your name?')

print "Hello " + name + " !"

original = raw_input("Enter a word: ")




if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  pyg = 'ay'
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)] 
  print new_word

else:
  print 'Not a word'
