from setuptools import setup

setup(
    name='webmsx-mkdocs-plugin',
    version='1.0.0',
    packages=['webmsx'],
    url='https://github.com/fmaida/hello-dolly-mkdocs-plugin',
    license='MIT',
    author='Francesco Maida',
    author_email='francesco.maida@gmail.com',
    description='Embed WebMSX emulator for use with mkdocs.',
    install_requires=['mkdocs'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'webmsx = webmsx:WMSXPlugin',
        ]
    },
)
