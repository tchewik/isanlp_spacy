from isanlp.processor_spacy import ProcessorSpaCy
from isanlp import PipelineCommon

def create_pipeline(delay_init=False):
    return PipelineCommon([(ProcessorSpaCy('ru_core_news_lg', morphology=True, parser=True, ner=True),
                              ['tokens', 'sentences'],
                              {'tokens' : 'tokens',
                               'sentences' : 'sentences',
                               'lemma': 'lemma',
                               'postag' : 'postag',
                               'morph' : 'morph',
                               'syntax_dep_tree' : 'syntax_dep_tree',
                               'entities': 'entities'}
                             )],
                            name='default')