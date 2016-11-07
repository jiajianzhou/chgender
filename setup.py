try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='chgender',
    version='0.0.2',
    description='Gender gusser for Chinese names in English (pinyin) form',
    long_description=open('README.md').read(),
    keywords='gender name guess python',
    url='https://github.com/jiajianzhou/chgender',
    author='Jiajian Zhou',
    author_email='jiajianzhou0808@gmail.com',
    packages=['chgender'],
    package_data={'':['*.md','*.txt'],
    'chgender': ['chinese_name_lib.txt','pinyin_dataset.txt']},
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],
    entry_points={
        'console_scripts': [
            'chg = chgender.batch:main',
        ],
    }
)
