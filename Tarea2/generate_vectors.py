import json
from os import listdir
from os.path import isfile, join
from load_config import load_config

if __name__ == "__main__":
  DATA_PATH = './json_data/'
  VECT_PATH = './vectors/'
  files = [ f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f)) ]
  """
    Load base files with entities, ignored files and categories for this example.
  """
  lc = load_config()
  lc.read_config()
  tokens = lc.get_entities()
  ignored_files = lc.get_ignored()
  CATEGORIES = lc.get_categories()
  files = [f for f in files if f not in ignored_files and '-key' not in f]
  for _file in files:
    keys = {}
    sfile = _file.split('.')
    json_key_file = open(DATA_PATH+sfile[0]+'-key.'+sfile[1], 'r')
    keys = json.loads(json_key_file.read())
    json_key_file.close()
    json_feature_file = open(DATA_PATH+sfile[0]+'.'+sfile[1], 'r')
    features = json.loads(json_feature_file.read())
    json_feature_file.close()

    end_file = open(VECT_PATH+sfile[0]+'-vec.txt', 'a')
    for feat_id in features:
      feature_1 = features[feat_id]['features_1']
      vector = str(feature_1['ES_TOKEN']) + ' '
      for feat_key in feature_1:
        if 'ES_TOKEN' not in feat_key and 'qid' not in feat_key:
          vector += str(keys[feat_key]) + ':' + str(feature_1[feat_key]) + ' '
        if 'PALABRA_' in feat_key:
          word = feat_key.split('PALABRA_')[1]
        if 'CAT_SINTACTICA_' in feat_key:
          cat = feat_key.split('CAT_SINTACTICA_')[1]
      vector += '# ' + feature_1['qid'].encode('utf-8') + ' ' + word.encode('utf-8') + ' ' + cat.encode('utf-8') + '\n'
      end_file.write(vector)
    end_file.close()