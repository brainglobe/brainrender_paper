from brainrender import Scene
from brainrender.atlas_specific import get_streamlines_for_region
from brainrender.actors.streamlines import Streamlines
from brainrender.actors import Points, Point, Volume
from brainrender.atlas_specific import GeneExpressionAPI

from rich import print
from oneibl.onelight import ONE

from myterial import blue_grey_darker, blue_grey, orange, salmon_light, salmon_darker, blue_grey_dark
from myterial import salmon_darker as inj1col
from myterial import salmon_light as inj2col
from myterial import salmon_dark as streamlinescol
from myterial import blue_grey_light as scmcol
from myterial import blue_grey as pagcol
from myterial import salmon_dark as neuroncol
from myterial import purple_dark as gene2_color
from myterial import purple_light as gene1_color

from scripts.utils import cameras

# -------------------------------- injections -------------------------------- #
def make_injections():
    scene = Scene()
    scene.root._silhouette_kwargs["lw"] = 1

    # add brain regions
    scm = scene.add_brain_region(
        "SCm", alpha=0.4, silhouette=False, color=blue_grey_darker
    )
    scm.wireframe()

    pag = scene.add_brain_region(
        "PAG", alpha=0.3, silhouette=False, color=blue_grey
    )
    pag.wireframe()

    # add injections
    fs = [
        "data/CC_134_2_ch1inj.obj",
        "data/CC_134_1_ch1inj.obj",
    ]
    cs = [
        inj1col,
        inj2col,
    ]
    injections = [scene.add(f, color=c) for f, c in zip(fs, cs)]
    scene.add(*injections)
    scene.add_silhouette(*injections, lw=2)
    
    scene.render(camera=cameras['f2p1'], zoom=3.5)
    scene.close()

# -------------------------------- Streamlines ------------------------------- #
def make_streamlines():
    scene = Scene()
    scene.root._silhouette_kwargs["lw"] = 1
    scene.root.alpha(0.5)

    # Add streamlines
    streams = get_streamlines_for_region("MOp")
    s = scene.add(Streamlines(streams[0], color=streamlinescol, alpha=1))

    # add nraom regopms
    th = scene.add_brain_region(
        "TH", alpha=0.45, silhouette=False, color=blue_grey
    )

    # slice scene
    scene.slice("horizontal", actors=[scene.root])

    scene.render(camera=cameras['f2p2'], zoom=2)
    scene.close()

# -------------------------------- neuropixels ------------------------------- #
def make_probes():
    scene = Scene()
    scene.root._silhouette_kwargs["lw"] = 1
    scene.root.alpha(0.2)

    # download probes data from IBL 
    one = ONE()
    one.set_figshare_url("https://figshare.com/articles/steinmetz/9974357")

    # select sessions with trials
    sessions = one.search(["trials"])

    # Get the location of implanted probes
    probes_locs = []
    for sess in sessions:
        probes_locs.append(one.load_dataset(sess, "channels.brainLocation"))

    # render a bunch of probes as sets of spheres (one per channel)
    for locs in probes_locs:
        k = int(len(locs) / 374.0)

        for i in range(k):
            points = locs[i * 374 : (i + 1) * 374]
            regs = points.allen_ontology.values

            if "LGd" in regs and ("VISa" in regs or "VISp" in regs):
                color = salmon_darker
                alpha = 1
                sil = 1
            elif "VISa" in regs:
                color = salmon_light
                alpha = 1
                sil = 0.5
            else:
                continue

            spheres = Points(
                points[["ccf_ap", "ccf_dv", "ccf_lr"]].values,
                colors=color,
                alpha=alpha,
                radius=30,
            )
            spheres = scene.add(spheres)

            if sil:
                scene.add_silhouette(spheres, lw=sil)


    # Add brain regions
    visp, lgd = scene.add_brain_region(
        "VISp",
        "LGd",
        hemisphere="right",
        alpha=0.3,
        silhouette=False,
        color=blue_grey_dark,
    )
    visa = scene.add_brain_region(
        "VISa", hemisphere="right", alpha=0.2, silhouette=False, color=blue_grey,
    )
    th = scene.add_brain_region(
        "TH", alpha=0.3, silhouette=False, color=blue_grey_dark
    )
    th.wireframe()
    scene.add_silhouette(lgd, visp, lw=2)


    scene.render(zoom=3.5, camera=cameras['f2p3'])
    scene.close()

# ------------------------------- single neuron ------------------------------ #
def make_single_neuron():
    scene = Scene(root=True)
    scene.root._needs_silhouette = False
    scene.root.alpha(0.5)

    # add brain regions
    pag = scene.add_brain_region("PAG", alpha=0.4, silhouette=False, color=pagcol)
    scm = scene.add_brain_region("SCm", alpha=0.3, silhouette=False, color=scmcol)


    # add neuron
    neuron = scene.add("data/single_neuron.stl")
    neuron.c(neuroncol)

    # add a sphere at the soma location
    soma_pos = [9350.51912036, 2344.33986638, 5311.18297796]
    point = scene.add(Point(soma_pos, color=neuroncol, radius=25))
    scene.add_silhouette(point, lw=1, color="k")
    scene.add_silhouette(neuron, lw=1, color="k")

    # slice to crop the image
    p = [9700, 1, 800]
    plane = scene.atlas.get_plane(pos=p, plane="frontal")
    scene.slice(plane, actors=[scm, pag, scene.root])

    p = [11010, 5000, 5705]
    plane = scene.atlas.get_plane(pos=p, norm=[0, -1, 0])
    scene.slice(plane, actors=[scene.root])

    scene.render(zoom=9, camera=cameras['f2p4'])
    scene.close()

# ------------------------------ gene expression ----------------------------- #
def make_zfish_genes():
    """
    Data downloaded from: https://fishatlas.neuro.mpg.de/lines/
    for this line: https://zfin.org/ZDB-ALT-050728-2

    data/T_AVG_brn3c_GFP.obj
    data/T_AVG_nk1688CGt_GFP.obj

    converted to mesh with
    ```python

        from brainio import brainio
        from vedo import Volume, write
        from bg_space import AnatomicalSpace
        from brainrender import Scene

        fp ='/Users/federicoclaudi/Downloads/T_AVG_Chat_GFP.tif'
        data = brainio.load_any(fp)

        s = Scene(atlas_name='mpin_zfish_1um')

        source_space = AnatomicalSpace("rai")
        target_space = s.atlas.space
        transformed_stack = source_space.map_stack_to(target_space, data)

        vol = Volume(transformed_stack, origin=s.root.origin()).medianSmooth()

        mesh = vol.isosurface().c('red').decimate().clean()
        write(mesh, 'data/T_AVG_Chat_GFP.obj')
    ```
    """
    SHIFT = [-20, 15, 30]  # fine tune posistion

    scene = Scene(
        atlas_name="mpin_zfish_1um", 
    )
    scene.root.alpha(0.2)

    # Add meshes showing gene expression, but fully transparent
    m = scene.add("data/T_AVG_nk1688CGt_GFP.obj", color=gene1_color, alpha=0)
    m2 = scene.add("data/T_AVG_brn3c_GFP.obj", color=gene2_color, alpha=0)

    for mesh in (m, m2):
        mesh.mesh.addPos(dp_x=SHIFT)

    # Create volumetric data from the meshes
    vol1 = Volume(m.density(), as_surface=True, min_value=20000, cmap="Reds")
    vol1.lw(1)
    scene.add(vol1)

    vol2 = Volume(m2.density(), as_surface=True, min_value=600, cmap="Blues")
    vol2.lw(1)
    scene.add(vol2)

    scene.render(camera=cameras['f2p5'], zoom=2.5)
    scene.close()

def make_mouse_genes():
    scene = Scene()
    scene.root._silhouette_kwargs["lw"] = 2
    scene.root.alpha(0.1)

    # Get gene expression data
    gene = "Gpr161"
    geapi = GeneExpressionAPI()

    expids = geapi.get_gene_experiments(gene)
    data = geapi.get_gene_data(gene, expids[1])

    gene_actor = geapi.griddata_to_volume(data, min_quantile=99, cmap="Reds")
    act = scene.add(gene_actor)

    # Add brain regions
    ca1 = scene.add_brain_region(
        "CA1", alpha=0.2, color=blue_grey_dark, silhouette=False
    )
    ca1.wireframe()


    scene.render(camera=cameras['f2p6'], zoom=3.5)
    scene.close()

# ----------------------------------- make ----------------------------------- #

def make():
    print(f'[{orange}]Making first panel')
    make_injections()

    print(f'[{orange}]Making second panel')
    make_streamlines()

    print(f'[{orange}]Making third panel')
    make_probes()

    print(f'[{orange}]Making fourth panel')
    make_single_neuron()

    print(f'[{orange}]Making fifth panel')
    make_zfish_genes()

    print(f'[{orange}]Making sixth panel')
    make_mouse_genes()