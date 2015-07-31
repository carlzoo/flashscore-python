from setuptools import setup

setup(name='flashscore',
      version='0.1',
      description='Package for fetching scores from Flashscores',
      url='https://github.com/carlzoo/flashscore-python',
      author='Carl Zhou',
      author_email='',
      license='MIT',
      packages=['flashscore'],
	  install_requires=[
          'dryscrape',
		  'BeautifulSoup4',
      ],
	  package_data={'flashscore': ['resources/*.txt']},
      zip_safe=False)
