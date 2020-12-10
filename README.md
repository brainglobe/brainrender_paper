# brainrender_paper
Code for recreating the figures in the brainrender paper (Claudi et al. 2020) titled: TITLE TO BE EDITED.

The [Claudi et al. 2020 paper](LINK TO BE EDITED) describes [the brainrender software](docs.brainrender.info) and the python code provided here can be used to recreate the figures in the paper.


### Figure 1
<img src='figures/Figure1.svg' max-width=1080px style="text-align:centered"></img>
> A) Brainrender’s design principles. Schematic illustration of how different types of data can be loaded into brainrender using either brainrender’s own functions, software packages from the BrainGlobe suite or custom Python scripts. All data loaded into brainrender is converted onto a unified format, which simplifies the process of visualizing data from different sources.  B) Using brainrender with different atlases. Visualization of brain atlas data from three different atlases using brainrender. Left, Allen atlas of the mouse brain showing the superficial (SCs) and motor (SCm) subdivisions of the superior colliculus and the Zona Incerta  (data from Wang et al. 2020).  Middle, visualization of the cerebellum (orange) and tectum (blue) in the larval zebrafish brain (data from Kunst et al. 2019). Right, visualization of the precentral gyrus, postcentral gyrus and temporal lobeof the human brain (data from Ding et al. 2016)  C) the brainrender GUI. Mouse, human and zebrafish larvae drawings from scidraw.io (doi.org/10.5281/zenodo.3925991, doi.org/10.5281/zenodo.3926189, doi.org/10.5281/zenodo.3926123,)


### Figure 2
<img src='figures/Figure2.svg' max-width=1080px style="text-align:centered"></img>
> Visualizing different types of data in brainrender. A) Spread of fluorescence labelling following viral injection of AAV2-CRE-eGPF in the superior colliculus of two FLEX-TdTomato mice. 3D objects showing the injection sites were created using custom python scripts following acquisition of a 3D image of the entire brain with serial 2-photon tomography and registration of the image data to the atlas’ template (with brainreg, Tyson, Rousseau, and Margrie 2020). B) Streamlines visualization of efferent projections from the mouse primary motor cortex following injection of an anterogradely transported virus expressing fluorescent proteins (original data from Oh et al. 2014, downloaded from Neuroinformatics NL with brainrender). C) Visualization of the location of several implanted neuropixel probes from multiple mice (data from Steinmetz et al. 2019). Dark salmon colored tracks show probes going through both primary/anterior visual cortex (VISp/VISa) and the dorsal lateral geniculate nucleus of the thalamus. D) Single periaqueductal gray (PAG) neuron. The PAG and superior colliculus are also shown. The neuron’s morphology was reconstructed by targeting the expression of fluorescent proteins in excitatory neurons in the PAG via an intersectional viral strategy, followed by imaging of cleared tissue and manual reconstruction of the neuron’s morphology with Vaa3D software. Data were registered to the Allen atlas with sharptrack (Shamash et al. 2018). The 3D data was saved as a .stl file and loaded directly into brainrender. E) Gene expression data. Left, expression of genes ‘brn3c’ and ‘nk1688CGt’ in the tectum of the larval zebrafish brain (gene expression data from fishatlas.neuro.mpg.de, 3D objects created with custom python scripts). Right, expression of gene ‘Gpr161’ in the mouse hippocampus (gene expression data from Wang et al. 2020, downloaded with brainrender. 3D objects created with brainrender). Colored voxels show voxels with high gene expressions. The CA1 field of the hippocampus is also shown.


### Figure 3
<img src='figures/Figure3.svg' max-width=1080px style="text-align:centered"></img>
>A) Visualizing the location of labelled cells. Left, visualization of fluorescently labelled cells identified using cellfinder (data from Tyson et al. 2020). Right, visualization of functionally defined clusters of regions of interest in the brain of a zebrafish larvae during a visuomotor task. (data from Markov et al. 2020).  B) Visualizing neuronal morphology data. Left. three secondary motor cortex neurons projecting to the thalamus (data from Winnubst et al. 2019, downloaded with morphapi from neuromorpho.org). Right, morphology of cerebellar neurons in larval zebrafish (data from Kunst et al. 2019, downloaded with morphapi). In the left panel of A) and B), the brain’s outline was sliced along the midline to expose the data.


## Installation
**This code was written in python==3.6.3 and brainrender==2.0.0.4, Installing this package will force brainrender to have version 2.0.0.4. If you don't want that to happen, don't use `pip install .`**. 

The easiest way to run the scripts in this repository is by cloning and installing it:
```
git clone https://github.com/brainglobe/brainrender_paper.git
cd brainrender_paper
pip install .
```

This will install all the requirements. This code was written for `brainrender` version `2.0.0.3`,  so to ensure that the scripts will run correctly running `pip install .` will install that version of the software. If you want to use a different version of brainrender, then **do not** use `pip install .` as that will force brainrender to version 2.0.0.3.

## Usage
The scripts in `scripts/figure_*.py` can be run to create each of the figures. In each of those scripts there's a function that takes care of creating each of the figure's panels. 

If you installed this repository with `pip install .`, you can run the `scripts/figure_*.py` script (from your terminal, with the anaconda environment where this repository was installed active)  with: `make_figure N` where N is a number in (1, 2, 3) specifying which figure should be made.

To make videos, you can run `make_video N` in your terminal.