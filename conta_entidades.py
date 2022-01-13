import spacy
import spacy.attrs
import pt_core_news_sm

from collections import Counter, OrderedDict


nlp = pt_core_news_sm.load()

def conta_entidade(df):
  text = ''
  for index, row in df.iterrows():
    text = text + row['titulo'] + ' '
        
  doc = nlp(text)

  palavras = {}

  labels = [x.text for x in doc.ents]
  dicionario = Counter(labels)

  palavras = OrderedDict(sorted(dicionario.items(), key = lambda kv : kv[1], reverse=True))
  return palavras
