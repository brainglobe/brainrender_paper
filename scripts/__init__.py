from brainrender import settings
import click
from myterial import salmon
from rich import print

from scripts.figure_1 import make as make_figure_1
from scripts.figure_2 import make as make_figure_2
from scripts.figure_3 import make as make_figure_3


funcs = {
    1:make_figure_1,
    2:make_figure_2,
    3:make_figure_3,
}

settings.SHOW_AXES = False
settings.LW = 2
settings.INTERACTIVE = True
settings.WHOLE_SCREEN = True
settings.SHADER_STYLE = "cartoon"
settings.ROOT_ALPHA = 0.3


@click.command()
@click.argument('fig_n')
def make(fig_n):
    print(f'[bold {salmon}]Making figure {fig_n}')
    funcs[int(fig_n)]()