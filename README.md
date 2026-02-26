# Autoantibody-quantification
This project quantifies autoantibody intensities in different subcellular regions. 

illm_correted.cpproj: This pipeline was created in [CellProfiler](https://cellprofiler.org/). It perfroms illumination correction for all the 4 image channels. Then it segments nucleolus, nucleus and cytoplasm from the respective channels for HeP2 cell images. Finally, it measures the autoantibody intensity in each of those segmented regions. 

tissue_seg_code.py: This is python code which segments the nucleus and cytoplasm in mouse tissues images and measures the autoanitbody intensity in those regions. 

The required packages can be found in pyproject.toml
