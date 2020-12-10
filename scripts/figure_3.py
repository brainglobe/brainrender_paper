from brainrender import Scene
from brainrender.actors import Points, Point
from morphapi.api.mouselight import MouseLightAPI
from morphapi.api.mpin_celldb import MpinMorphologyAPI

from rich import print
import pandas as pd
import h5py
from random import choice
from rich.progress import track

from myterial import orange, salmon, salmon_dark, salmon_darker, orange_darker, grey_darker
from myterial import blue_grey as thcol
from myterial import blue_grey_dark as thcol2
from myterial import salmon as c1
from myterial import orange_darker as c2
from myterial import indigo as c3
from myterial import salmon as z1
from myterial import blue_light as z2
from scripts.utils import cameras


# ----------------------------------- cells ---------------------------------- #
def make_mouse_cells():
    scene = Scene()

    # Load and add cells
    coords = pd.read_hdf("data/cell-detect-paper-cells.h5")
    cells = scene.add(
        Points(coords[["x", "y", "z"]].values, radius=30, colors=salmon)
    )
    scene.add_silhouette(cells, lw=1)

    # add brain regions
    scene.add_brain_region("TH", alpha=0.2, silhouette=False, color=thcol)

    # cut and render
    scene.slice("sagittal")
    scene.render(camera="sagittal", zoom=2.6)
    scene.close()

def make_zfish_cells():
    cluster_data = h5py.File("data/zfish_rois_clusters.h5", "r")
    cluster_ids = cluster_data["cluster_ids"][:]
    roi_coords = cluster_data["coords"][:]

    scene = Scene(
        atlas_name="mpin_zfish_1um"
    )

    # add cells
    colors = [c1, c2, c3]
    for i, col in enumerate(colors):
        rois_in_cluster = roi_coords[cluster_ids == i, :]
        coords = pd.DataFrame(rois_in_cluster, columns=["x", "y", "z"]).values

        pts = scene.add(Points(coords, colors=col, radius=2, alpha=1))
        scene.add_silhouette(pts, lw=1)

    scene.render(camera=cameras['f3p2'], zoom=2.5)
    scene.close()


# ------------------------------- morphologies ------------------------------- #
def make_mouse_morphologies():
    scene = Scene()

    # download neurons data
    mlapi = MouseLightAPI()
    neurons_metadata = mlapi.fetch_neurons_metadata(
        filterby="soma", filter_regions=["MOs"]
    )

    to_add = [neurons_metadata[47], neurons_metadata[51], neurons_metadata[60]]
    neurons = mlapi.download_neurons(to_add, soma_radius=500)

    # add neurons to scene
    colors = (salmon_dark, salmon_darker, orange_darker)
    for neuron, color in zip(neurons, colors):
        meshes = neuron.create_mesh(soma_radius=35, neurite_radius=10)[0]
        dendrites = scene.add(meshes["basal_dendrites"], color=grey_darker)
        soma = scene.add(meshes["soma"], color=grey_darker)
        axon = scene.add(meshes["axon"], color=color)


    # add brain regions, slice and render
    th = scene.add_brain_region("TH", alpha=0.1, color=thcol2)
    scene.slice("sagittal", actors=[scene.root, th])

    scene.render(zoom=2.4, camera=cameras['f3p3'])
    scene.close()

def make_zfish_morphologies():
    scene = Scene(
        atlas_name="mpin_zfish_1um"
    )
    scene.root.alpha(0.2)
   
    # download neurons
    api = MpinMorphologyAPI()
    neurons_ids = api.get_neurons_by_structure(837)
    neurons = api.load_neurons(neurons_ids)
    neurons = [
        neuron.create_mesh(soma_radius=0.75, neurite_radius=1)
        for neuron in neurons
    ]

    # add neurons to the scene
    for (neu_dict, neu) in track(neurons, total=len(neurons)):
        col = choice((z1, z2))
        neuron = scene.add(neu_dict["axon"], alpha=1, color=col)

        soma = scene.add(
            Point(neu_dict["soma"].centerOfMass(), color=col, radius=8, alpha=1)
        )
        scene.add_silhouette(soma)

    # render
    scene.render(zoom=1.7, camera=cameras['f3p4'])
    scene.close()


def make():
    print(f'[{orange}]Making first panel')
    make_mouse_cells()

    print(f'[{orange}]Making second panel')
    make_zfish_cells()

    print(f'[{orange}]Making third panel')
    make_mouse_morphologies()

    print(f'[{orange}]Making fourth panel')
    make_zfish_morphologies()