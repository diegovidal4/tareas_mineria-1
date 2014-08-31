import MontyLemmatiser
import MontyTagger
p = MontyLemmatiser.MontyLemmatiser()
m=MontyTagger.MontyTagger(0)

def has_root(word):
  root = map(lambda the_tokenizer_str:p.lemmatise_word(the_tokenizer_str,), word.split())
  if root[0] != word:
    return 1
  else:
    return 0

def full_upper(word):
  if word.isupper():
    return 1
  else:
    return 0

def full_lower(word):
  if word.islower():
    return 1
  else:
    return 0

def is_capitalized(word):
  is_cap = True
  if word[0].isupper():
    for l in word[1:]:
      if l.islower() and is_cap != False:
        is_cap = True
      else:
        is_cap = False
  else:
    return 0
  if is_cap:
    return 1
  else:
    return 0

def sin_cat(word):
  tag = m.tag(word, 0, 0)
  cat = tag.split('/')[1]
  return cat

def word_len(word):
  return len(word)

def is_token(word, tokens):
  token = False
  for tok in tokens:
    if tok in word:
      token = True
      break

  if token:
    return 1
  else:
    return 0
