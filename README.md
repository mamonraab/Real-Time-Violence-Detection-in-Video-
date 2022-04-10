[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/robust-real-time-violence-detection-in-video/video-classification-on-hockey-fight)](https://paperswithcode.com/sota/video-classification-on-hockey-fight?p=robust-real-time-violence-detection-in-video)


# Real Time Violence Detection in Video
#
The source code associated with the paper [ Robust Real-Time Violence Detection in Video Using CNN And LSTM ](https://ieeexplore.ieee.org/document/8852616)

for simple demo please see this video https://www.youtube.com/watch?v=qeFrjFa5Rxc

the trained wights  can be downloaded from this url  https://drive.google.com/file/d/11IN2npH3i8PhzECNMcxfIQNFWPROr5gt/view?usp=sharing


Detection of a violence event in surveillance systems is playing a significant role in law enforcement and city safety. The effectiveness of violence event detectors measures by the speed of response and the accuracy and the generality over different kind of video sources with a different format. Several studies worked on the violence detection with focus either on speed or accuracy or both but not taking into account the generality over different kind of video sources. In this paper, we proposed a real-time violence detector based on deep-learning methods. The proposed model consists of CNN as a spatial feature extractor and LSTM as temporal relation learning method with a focus on the three-factor (overall generality - accuracy - fast response time). The suggested model achieved 98% accuracy with speed of 131 frames/sec. Comparison of the accuracy and the speed of the proposed model with previous works illustrated that the proposed model provides the highest accuracy and the fastest speed among all the previous works in the field of violence detection.

## please use Tensorflow version 2.0.0 ,  the other dependencies is  numpy   skimage.io   opencv  PIL , BytesIO , time

## training wight on kaggle https://www.kaggle.com/datasets/iraqai/violencewights-combo94-cnn-lstm
## full usage example on kaggle https://www.kaggle.com/code/iraqai/real-time-violence-detection-in-video

##  if you use pytorch i build another model with pytorch   you can found it here  https://github.com/mamonraab/violance-detection-in-video-with-pytroch


To cite our paper/code:

```
@INPROCEEDINGS{8852616,
author={A. R. {Abdali} and R. F. {Al-Tuma}},
booktitle={2019 2nd Scientific Conference of Computer Sciences (SCCS)},
title={Robust Real-Time Violence Detection in Video Using CNN And LSTM},
year={2019},
volume={},
number={},
pages={104-108},
keywords={convolutional neural nets;feature extraction;learning (artificial intelligence);video signal processing;CNN;violence event detector measures;overall generality;accuracy factor;fast response time;temporal relation learning method;deep-learning methods;real-time violence detector;video sources;city safety;law enforcement;surveillance systems;LSTM;robust real-time violence detection;CNN;LSTM;Violence Detection;Smart Cities;Deep Learning},
doi={10.1109/SCCS.2019.8852616},
ISSN={null},
month={March},}

```
