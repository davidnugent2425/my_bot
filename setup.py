from setuptools import setup

package_name = 'my_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Your Name',
    author_email='your.email@example.com',
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='A simple image subscriber node for ROS 2.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_subscriber = my_bot.image_subscriber:main',
        ],
    },
)
