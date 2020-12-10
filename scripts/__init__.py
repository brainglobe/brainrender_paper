from brainrender import settings
import click
from myterial import salmon, orange
from rich import print

from scripts.figure_1 import make as make_figure_1
from scripts.figure_2 import make as make_figure_2
from scripts.figure_3 import make as make_figure_3

from scripts.video_1 import make as make_video_1
from scripts.video_2 import make as make_video_2
from scripts.video_3 import make as make_video_3
from scripts.video_4 import make as make_video_4


funcs = {
    1:make_figure_1,
    2:make_figure_2,
    3:make_figure_3,
}

vid_funcs = {
    1:make_video_1,
    2:make_video_2,
    3:make_video_3,
    4:make_video_4,
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


# @click.command()
# @click.argument('vid_n')
def make_video(vid_n):
    print(f'[{orange}]Making video {vid_n}')
    vid_funcs[int(vid_n)]()
