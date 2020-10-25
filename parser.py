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
text = 'Мама мыла раму в сапогах, ветер дул в окно.'
doc = Doc(text)
doc.segment(segmenter)
#display(doc.tokens[:5])
#display(doc.sents[:5])
doc.tag_morph(morph_tagger)
#display(doc.tokens[:5])
#doc.sents[0].morph.print()
for token in doc.tokens:
    token.lemmatize(morph_vocab)
    
#display(doc.tokens[:5])
{_.text: _.lemma for _ in doc.tokens}
doc.parse_syntax(syntax_parser)
display(doc.tokens[:10])
doc.sents[0].syntax.print()
