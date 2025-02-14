from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,

    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)
names_extractor = NamesExtractor(morph_vocab)
text = 'Собака была съедена'
doc = Doc(text)
doc.segment(segmenter)
#display(doc.tokens[:5])
#display(doc.sents[:5])
doc.tag_morph(morph_tagger)
#display(doc.tokens[:5])
#doc.sents[0].morph.print()
for token in doc.tokens:
    token.lemmatize(morph_vocab)
    
display(doc.tokens[:10])
{_.text: _.lemma for _ in doc.tokens}
doc.parse_syntax(syntax_parser)
#display(doc.tokens[:10])
#doc.sents[0].syntax.print()
s = []
znaki = [',', '.', '!', '?']
znak = 0
znak = (len([x for x in text if x in ',.!?']))

slov = len(text.split())
s = doc.tokens[:(slov+znak)]
print()
i=0
count = 0
massiv = []
heads = []
used = []
all = [ [],[] ]
rootid = []
verb = []
while(i<(slov+znak)):
  o = str(s[i]);
  x1=o.find("rel=", 0,len(o))+5
  x2=o.find("'",x1,len(o))
  rel=o[x1:x2]
  x1=o.find("id=", 0,len(o))+6
  x2=o.find("'",x1,len(o))
  id=o[x1:x2]
  x1=o.find("text=", 0,len(o))+6
  x2=o.find("'",x1,len(o))
  textn=o[x1:x2]
  if (rel == 'root' or rel == 'conj' or rel == 'acl:relcl'): 
    verb.append(id)
    verb.append(textn)
    rootid.append(id)
  if (rel == 'parataxis'):
    heads.append(id)
  i+=1
print(heads)
i=0
masss = []
mass = [[],[]]
while (i<(slov+znak)):
  print(s[i])
  o = str(s[i]);
  x1=o.find("id=", 0,len(o))+6
  x2=o.find("'",x1,len(o))
  id=o[x1:x2]
  x1=o.find("text=", 0,len(o))+6
  x2=o.find("'",x1,len(o))
  textn=o[x1:x2]
  x1=o.find("head_id", 0,len(o))+11
  x2=o.find("'",x1,len(o))
  headid=o[x1:x2]

  x1=o.find("rel=", 0,len(o))+5
  x2=o.find("'",x1,len(o))
  rel=o[x1:x2]

  massiv.append(id)
  massiv.append(headid)
  massiv.append(textn)
  massiv.append(rel)
  print(massiv)
  subjp = ''
  aux=''
  if (headid in rootid and ( rel == 'nsubj' or rel == 'obj' or rel == 'iobj' or rel == 'aux:pass' or rel == 'nsubj:pass') ): 
    noun = textn
    if headid in verb:
      verba = verb.index(headid)
      if (rel == 'aux:pass' or rel == 'nsubj:pass'):
        if rel == 'aux:pass':
          aux=textn+' ' + verb[verba+1]
          used.append(headid)
        if rel == 'nsubj:pass':
          subjp = noun
      if (rel == 'iobj' and headid not in used):
        mass.append(['',verb[verba+1]])
      if (rel == 'nsubj'):
        verba = verb.index(headid)
        mass.append([noun,verb[verba+1]])
        used.append(headid)
    else:
      if (rel == 'nsubj'):
        mass.append([noun,''])
  if (aux!='' or subjp!=''):
    massiv.append([aux, subjp])
  if (rel != 'parataxis' and (headid not in heads)):
    all.append(massiv)
  massiv =[]
  i+=1
all.pop(1)
all.pop(0)
mass.pop(1)
mass.pop(0)
print()
i=0
print(mass)
print(all)
