from setuptools import setup

setup(name='Gojira',
      version='0.1',
      description='Command line interface and macros for Jira',
      url='https://github.com/SaltyCatFish/gojira',
      author='Ryan Long',
      author_email='ryan@saltycatfish.com',
      license='MIT',
      packages=['gojira'],
      entry_points={
          'console_scripts': ['gojira=gojira.cli:cli'],
      },
      install_requires=[
          'asn1crypto==0.24.0',
          'certifi==2018.11.29',
          'cffi==1.11.5',
          'chardet==3.0.4',
          'Click==7.0',
          'cryptography==2.4.2',
          'defusedxml==0.5.0',
          'idna==2.8',
          'invoke==1.2.0',
          'jira==2.0.0',
          'oauthlib==2.1.0',
          'pbr==5.1.1',
          'pip==18.1',
          'pycparser==2.19',
          'PyJWT==1.7.1',
          'requests==2.21.0',
          'requests-oauthlib==1.0.0',
          'requests-toolbelt==0.8.0',
          'setuptools==40.6.3',
          'six==1.12.0',
          'tabulate==0.8.2',
          'urllib3==1.24.2',
          'wheel==0.32.3',
          'prompt-toolkit==2.0.7',
          'Pygments==2.7.4'
      ],
      zip_safe=False)
