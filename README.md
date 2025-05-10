# Slice-Level Attention Module (SLAM)
This respository contains the code of my final degree project in Biomedical Engeneering. The work is about the detection of breast cancer in tomosynthesis images using deep learning. 
For that is has been taken the architecture Faster R-CNN as a baseline and added, in a ResNet50 backbone, a simple atention module for detecting the most representative slice. With the weights obtained by this module, the number of feature maps is reduced to one, so the data used in the Faster R-CNN is very low for a 3D image. 

For more information, the final degree project is also in this repository.



