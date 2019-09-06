# -*- coding: utf-8 -*-
# pylint: disable=protected-access

import itertools

from django import test

import testarossa


# Lisää Django-testityökalut Testarossa-moduuliin
list(itertools.starmap(testarossa.__dict__.setdefault, test.__dict__.items()))


def django(testi):
  if 'fixtures' in testi:
    return {
      '__class__': testi.pop('__class__', test.TestCase),
      **testi,
    }
  return testi
django.ennen = '__all__'
