# -*- coding: utf-8 -*-

import setuptools

setuptools._install_setup_requires({'setup_requires': ['git-versiointi']})
from versiointi import asennustiedot

setuptools.setup(
  name='testarossa-django',
  packages=setuptools.find_packages(),
  include_package_data=True,
  zip_safe=False,
  entry_points={
    'testarossa.laajennos': [
      'django = tr_django:django',
    ],
  },
  **asennustiedot(__file__),
)
