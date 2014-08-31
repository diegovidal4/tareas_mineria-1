from utils import is_capitalized, full_upper, full_lower, has_root, sin_cat, word_len

def all_occurences(stext, word):
  index = 0
  idx_list = []
  for st in stext:
    if st == word:
      idx_list.append(index)
    index += 1
  return idx_list

def create_side(words, side, tmp_bow):
  if side == 'left':
    key = 'IZQUIERDA_'
    key_cat = 'IZQUIERDA_CAT_'
  elif side == 'right':
    key = 'DERECHA_'
    key_cat = 'DERECHA_CAT_'
  for w in words:
    key += key+str(w)
    cat = sin_cat(w)
    key_cat += key_cat+cat
    if w != '':
      tmp_bow[key] = 1
      tmp_bow[key_cat] = 1
    if key in tmp_bow:
      tmp_bow[key] += 1
    if key_cat in tmp_bow:
      tmp_bow[key_cat] += 1
  return tmp_bow

def create_main_feature(word, token):
  tmp_bow = {}
  tmp_bow['TIENE_RAIZ'] = has_root(word)
  tmp_bow['FULL_MAYUSCULAS'] = full_upper(word)
  tmp_bow['FULL_MINUSCULAS'] = full_lower(word)
  tmp_bow['INICIO_MAYUSCULAS_RESTO_MINUSCULAS'] = is_capitalized(word)
  tmp_bow['CAT_SINTACTICA_'+ sin_cat(word)] = 1
  tmp_bow['PALABRA_'+word] = 1
  tmp_bow['PALABRA_LARGO'] = word_len(word)
  tmp_bow['ES_TOKEN'] = token
  return tmp_bow

def create_second_feature(index, text):
  """
    this function processes the context of the word,
    we analyze the right and left side of the word,
    try to look the features of the word that we find.
  """
  tmp_bow = {}
  stext = text.split()
  # left side
  words = []
  words.append(stext[index-3])
  words.append(stext[index-2])
  words.append(stext[index-1])
  tmp_bow = create_side(words, 'left', tmp_bow)
  # right side
  words = []
  words.append(stext[index+3])
  words.append(stext[index+2])
  words.append(stext[index+1])
  tmp_bow = create_side(words, 'right', tmp_bow)
  return tmp_bow

def create_third_feature(word, text):
  """
    this function processes the context of the word,
    we analyze the right and left side of the word,
    try to look the features of the word that we find.
    Same as previous function but new we look on the global scope.
  """
  tmp_bow = {}
  stext = text.split()
  index = all_occurences(stext, word)
  for idx in index:
    # left side
    words = []
    words.append(stext[idx-3])
    words.append(stext[idx-2])
    words.append(stext[idx-1])
    tmp_bow = create_side(words, 'left', tmp_bow)
    # right side
    words = []
    words.append(stext[index+3])
    words.append(stext[index+2])
    words.append(stext[index+1])
    tmp_bow = create_side(words, 'right', tmp_bow)
  return tmp_bow

def create_fourth_feature():
  pass



