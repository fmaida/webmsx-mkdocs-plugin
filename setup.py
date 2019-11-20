from setuptools import setup

setup(
    name='webmsx-mkdocs-plugin',
    version='0.9.12',
    packages=['webmsx'],
    url='https://github.com/fmaida/webmsx-mkdocs-plugin',
    license='MIT',
    author='Francesco Maida',
    author_email='francesco.maida@gmail.com',
    description='Embed WebMSX emulator in mkdocs documents.',
    install_requires=['mkdocs'],
    include_package_data=True,
    
    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'webmsx = webmsx:WebMSXPlugin',
        ]
    },
)
