import setuptools

setuptools.setup(
    name='rss_reader',
    version='4.0',
    author='Vlad Sheydenkov',
    author_email='vladsheydenkov@gmail.com',
    url='https://github.com/vladsheydenkov/PythonFinalTask.git',
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=['requests', 'bs4', 'feedparser', 'lxml', 'reportlab', 'jinja2', 'python-dateutil'],
    entry_points={
        'console_scripts': ['rss_reader=rss_reader.rss_reader_main:main'],
    }
)
