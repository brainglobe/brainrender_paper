from brainrender import Scene
from rich import print

# Colors for various meshes
from myterial import orange
from myterial import indigo as scmcol
from myterial import indigo_dark as scscol
from myterial import blue_darker as zicol
from myterial import cyan as cbcol
from myterial import teal as tcol
from myterial import salmon_dark as br1
from myterial import amber as br2
from myterial import orange_dark as br3

from scripts.utils import cameras

# ------------------------------- mouse regions ------------------------------ #

def mouse_regions():
    scene = Scene(inset=False)

    for reg, col in zip(("SCm", "SCs", "ZI"), (scmcol, scscol, zicol)):
        scene.add_brain_region(reg, color=col)


    scene.render(zoom=1.75, camera=cameras['f1p1'])
    scene.close()

# ------------------------------- zfish regions ------------------------------ #

def zfish_regions():
    scene = Scene(
        inset=False,atlas_name="mpin_zfish_1um"
    )
    scene.root._silhouette_kwargs["lw"] = 3
    scene.root.alpha(0.2)

    cb, t = scene.add_brain_region("cerebellum", "tectum")
    cb.c(cbcol)
    t.c(tcol)

    scene.render(zoom=1.9, camera=cameras['f1p2'])
    scene.close()

# ------------------------------- human regions ------------------------------ #

def human_regions():
    scene = Scene(
    inset=False, atlas_name="allen_human_500um",
    )

    for main in ("TemL",):   # add subregionsof TTem
        subs = scene.atlas.get_structure_descendants(main)
        for sub in subs:
            reg = scene.add_brain_region(sub, color=br1)

    # add more regions
    scene.add_brain_region('PrCG', color=br2)
    scene.add_brain_region('PoCG', color=br3)

    scene.render(camera=cameras['f1p3'], zoom=1.65)
    scene.close()

def make():
    print(f'[{orange}]Making first panel')
    mouse_regions()
    
    print(f'[{orange}]Making second panel')
    zfish_regions()
    
    print(f'[{orange}]Making third panel')
    human_regions()
