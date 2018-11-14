from setuptools import setup

setup(
    name='solar_system_script',
    version='0.1',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    package_data = {
        # If any package contains *.txt or *.yaml, include them:
        '': ['*.yaml',],
    },
    include_package_data=True,
    packages=['my_solar_system',
              'plugin_samples',
              'config_samples',
             ],
    scripts=['my_solar_system/alignment.py'],
    install_requires=['pyyaml'],
)
