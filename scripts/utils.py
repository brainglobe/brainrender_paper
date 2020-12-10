from vedo import Box

def root_box(scene):
    '''
        Creates a transparent box around the root, 
        to ensure that camera movements are smooth
        during video creation
    '''
    pos = scene.root.centerOfMass()
    bounds = scene.root.bounds()
    bds = [
        bounds[1] - bounds[0],
        bounds[3] - bounds[2],
        bounds[5] - bounds[4],
    ]

    scene.add(
        Box(
            pos=[pos[0] - 1300, pos[1] - 500, pos[2]],
            length=bds[0],
            width=bds[1],
            height=bds[2],
        ).alpha(0),
        names="box",
        br_classes="box",
    )


# ---------------------------------- Cameras --------------------------------- #

f1p1 = {
        "pos": (-20268, -6818, 14964),
        "viewup": (0, -1, 0),
        "clippingRange": (16954, 58963),
        "focalPoint": (6489, 4329, -5556),
        "distance": 35514,
    }

f1p2 = {
    "pos": (-1122, -389, 1169),
    "viewup": (0, -1, 0),
    "clippingRange": (1168, 3686),
    "focalPoint": (469, 221, -346),
    "distance": 2280,
    }

f1p3 = {
    "pos": (232278, 99919, -189689),
    "viewup": (0, -1, 0),
    "clippingRange": (615, 1371),
    "focalPoint": (232763, 99854, -188877),
    "distance": 949,
    }

f2p1 = {
    "pos": (-19159, -6934, -37563),
    "viewup": (0, -1, 0),
    "clippingRange": (24191, 65263),
    "focalPoint": (7871, 2905, -6646),
    "distance": 42229,
}

f2p2 = {
    "pos": (9475, -39398, -5604),
    "viewup": (0, 0, -1),
    "clippingRange": (34734, 54273),
    "focalPoint": (7150, 3510, -5283),
    "distance": 42972,
}

f2p3 = {
    "pos": (-16170, -7127, 31776),
    "viewup": (0, -1, 0),
    "clippingRange": (27548, 67414),
    "focalPoint": (7319, 2861, -3942),
    "distance": 43901,
}

f2p4 = {
    "pos": (-16954, 2456, -3961),
    "viewup": (0, -1, 0),
    "clippingRange": (22401, 34813),
    "focalPoint": (7265, 2199, -5258),
    "distance": 24256,
}

f2p5 = {
        "pos": (-835, -1346, 1479),
        "viewup": (0, -1, 0),
        "clippingRange": (1703, 3984),
        "focalPoint": (334, 200, -342),
        "distance": 2660,
    }

f2p6 = {
    "pos": (-19159, -6934, -37563),
    "viewup": (0, -1, 0),
    "clippingRange": (24191, 65263),
    "focalPoint": (7871, 2905, -6646),
    "distance": 42229,
}


f3p2 = {
    "pos": (-890, -1818, 979),
    "viewup": (1, -1, -1),
    "clippingRange": (1773, 4018),
    "focalPoint": (478, 210, -296),
    "distance": 2759,
}

f3p3 = {
    "pos": (5892, 1302, 23377),
    "viewup": (0, -1, 0),
    "clippingRange": (22662, 41078),
    "focalPoint": (5943, 3955, -5680),
    "distance": 29178,
}

f3p4 = {
    "pos": (-890, -1818, 979),
    "viewup": (1, -1, -1),
    "clippingRange": (1773, 4018),
    "focalPoint": (478, 210, -296),
    "distance": 2759,
}



cameras = {
    'f1p1':f1p1,
    'f1p2':f1p2,
    'f1p3':f1p3,
    'f2p1':f2p1,
    'f2p2':f2p2,
    'f2p3':f2p3,
    'f2p4':f2p4,
    'f2p5':f2p5,
    'f2p6':f2p6,
    'f3p2':f3p2,
    'f3p3':f3p3,
    'f3p4':f3p4,
}

