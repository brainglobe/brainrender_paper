from setuptools import setup, find_namespace_packages

requirements = ['brainrender==2.0.0.3', 'ibllib']

setup(
    name='brainrender_figures',
    version='1.0',
    description="Figures for Claudi et al 2020",
    packages=find_namespace_packages(),
    install_requires=requirements,

    entry_points={
        'console_scripts': [
            'make_figure = scripts.__init__:make',
        ],
    },
    url="https://github.com/brainglobe/brainrender_paper",
    author="Federico Claudi, Adam Tyson, Luigi Petrucco",
    zip_safe=False,
)