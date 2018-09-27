# -*- coding: utf-8 -*-
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import provider


items = [ ('low', u'secret'),
          ('mid', u'more secret'),
          ('height', u'most secret')          
          ]
terms = [ SimpleTerm(value=pair[0], token=pair[0], title=pair[1]) for pair in items ]
Vocabulary = SimpleVocabulary(terms)

@provider(IVocabularyFactory)
def safe_level_factory(context):
    return Vocabulary