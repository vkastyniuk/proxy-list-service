from setuptools import setup

setup(
    name='proxy_service',
    version='0.0.1',
    url='https://vkastyniuk@github.com/vkastyniuk/proxy-list-service.git',
    packages=['proxy_service'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
    ],
    zip_safe=False
)
