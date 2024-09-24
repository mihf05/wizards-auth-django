from setuptools import setup, find_packages

setup(
    name='wizards-outh-django',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Django>=3.2',
        'djangorestframework>=3.12',
        'djangorestframework-simplejwt>=4.6',
        'django-cors-headers>=3.7',
        'django-allauth>=0.44',
        'django-login-history2==0.0.6',
    ],
    author='MD IRFAN HASAN FAHIM',
    author_email='mdirfanhasanfahim@gmail.com',
    description='A powerful authentication API using Django, similar to Clerk.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mihf05/wizards-auth-django.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
