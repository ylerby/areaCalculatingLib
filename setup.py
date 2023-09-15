from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
  name='speedfile',
  version='0.0.1',
  author='ylerby',
  author_email='WeaklyFob@yandex.ry',
  description='library for finding the area of a circle and a triangle',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='your_url',
  packages=find_packages(),
  install_requires=["pytest"],
  classifiers=[
    'Programming Language :: Python :: 3.9',
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'your_github'
  },
  python_requires='>=3.6'
)