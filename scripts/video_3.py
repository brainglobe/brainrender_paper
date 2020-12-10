from brainrender import Scene, Animation

from scripts.utils import root_box

def make():
    scene = Scene()

    root_box(scene)
    mains = (
        "Isocortex",
        "HPF",
        "STR",
        "PAL",
        "CB",
        "MB",
        "TH",
        "HY",
        "P",
        "MY",
        "CTXsp",
        "OLF",
        "VISC",
    )

    for main in mains:
        subs = scene.atlas.get_structure_descendants(main)
        for sub in subs:
            try:
                reg = scene.add_brain_region(sub)
            except FileNotFoundError:
                pass


    def slc(scene, framen, totframes):
        # remove silhouettes
        scene.remove(*scene.get_actors(br_class="silhouette"))

        # Get new slicing plane
        fact = framen / totframes
        point = [14000 * fact, 4000, 6000]
        plane = scene.atlas.get_plane(pos=point, norm=(1, 0, 0))

        # slice
        box = scene.get_actors(name="box")[0]
        acts = [a for a in scene.actors if a != box]
        scene.slice(plane, actors=acts)

        # make new silhouettes
        for act in scene.get_actors(br_class="brain region"):
            act._needs_silhouette = True


    # ----------------------------- create animation ----------------------------- #
    anim = Animation(scene, "videos", "video_three", size=None)

    # Specify camera pos and zoom at some key frames`
    anim.add_keyframe(0, camera="frontal", zoom=1.5, callback=slc, duration=10)

    # Make videos
    anim.make_video(duration=10, fps=30)
