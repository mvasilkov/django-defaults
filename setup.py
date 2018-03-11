from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(name='django-defaults',

          version='0.0.0',

          description='Django settings sans boilerplate',
          long_description='Django settings sans boilerplate',

          url='https://github.com/mvasilkov/django-defaults',

          author='Mark Vasilkov',
          author_email='mvasilkov@gmail.com',

          license='MIT',

          classifiers=[
              'Framework :: Django',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: MIT License',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3 :: Only',
          ],

          keywords='django settings toml',

          packages=find_packages(),

          install_requires=['toml'])
