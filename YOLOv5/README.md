#Attention Mechanisms and YOLOv5

Instructions on how to find the code I wrote is below (for attention):

There are two folder, one for each attention mechanism. Each folder has a Jupyter notebook, that shows the training performance and metrics.

Attention mechanisms can be found at the bottom of the file models/common.py and are appropriately named.

Please see the function parse_model() in the file: models/yolo.py to see how the attention mechanisms are ncorporated into the learning function.

The backbone changes can be found in the YAML file location in models. The YAML file for SENet is named: 'yolov5_SE_Atten.YAML' and the file for the co-ordinatte attention is named: 