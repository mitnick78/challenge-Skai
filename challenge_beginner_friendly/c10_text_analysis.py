sentence_input = input("Enter a sentence: ")

def count_vowels_consonants(sentence):
  vowels = "aeiouAEIOU"
  consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
  num_vowels = 0
  num_consonants = 0

  for char in sentence:
    if char in vowels:
      num_vowels += 1
    elif char in consonants:
      num_consonants += 1
      
    num_words = len(sentence.split())
  
  return num_vowels, num_consonants, num_words


words, vowels, consonants = count_vowels_consonants(sentence_input)

print(f"Number of words: {words}")
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")

