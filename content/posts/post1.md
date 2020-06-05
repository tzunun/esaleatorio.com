---
title: "Recovering 3D Editable Objects from a Single Photograph" 
date: 2020-06-05 
draft: false 
---

Story source:

https://chenxin.tech/files/Paper/TVCG2018_AutoSweep/AutoSweep.html


# AutoSweep: Recovering 3D Editable Objects  
from a Single Photograph

![figure](./WebPage/image/AutoSweep_tesar.jpg)

# Abstract

* * *

This paper presents a fully automatic framework for extracting editable 3D
objects directly from a single photograph. Unlike previous methods which
recover either depth maps, point clouds, or mesh surfaces, we aim to recover
3D objects with semantic parts and can be directly edited. We base our work on
the assumption that most human-made objects are constituted by parts and these
parts can be well represented by generalized primitives. Our work makes an
attempt towards recovering two types of primitive-shaped objects, namely,
generalized cuboids and generalized cylinders. Qualitative and quantitative
experiments show that our algorithm can recover high quality 3D models and
outperforms existing methods in both instance segmentation and 3D
reconstruction.

  

[[Paper](./AutoSweep_TVCG2018_paper.pdf)]
[[Video](./AutoSweep_TVCG2018_video.mp4)] [[BibTex](./xin2018autosweep.bib)]

# Pipeline

* * *

![figure](./WebPage/image/AutoSweep_whole_pipeline.jpg) The whole pipeline.
Our method takes as input a single photograph and extracts its semantic part
masks labeled as cylinder profile, cuboid profile, cylinder body, etc., which
are then used in a sweeping procedure to construct a textured 3D model.

  
  
  

![figure](./WebPage/image/AutoSweep_network_pipeline.jpg) The network
structure. The structure of our GeoNet is composed by an instance segmentation
network (Mask R-CNN) and a deformable convolutional network. The net outputs
instance masks labeled as semantic parts (profiles, bodies).

# Dataset

* * *

#### Download

You can download our dataset with [_this Onedrive
link_](https://1drv.ms/u/s!AsWCggO4PIEBnJ03gUFbEytQErI8Nw?e=f9Iwkl).

#### Part 1: Image

This folder in our dataset is including 11657 images with cubes and cylinders.
The real dataset contains about 6000 unannotated images from
[ImageNet](http://www.image-net.org/), 774 annotated images from [Xiao et
al.](http://3dvision.princeton.edu/projects/2012/SUNprimitive/), and 4883
images collected from the Internet.

#### Part 2: Annotation

Annotation of each image by segmentation label methods: We use color to encode
the instance and label information.

  * Red channel: {10,20,...} represents {instance 1, instance 2,...}.
  * Blue channel: zero represents body, nonzero represents top face.
  * Red channel: 150 represents grip, 200 represents cylinder, 255 represents cube.

Example is like below:

Label | Color | instance ID  
---|---|---  
Cylinder - top face | (10, 10, 200) | 1  
Cylinder - top face | (20, 20, 200) | 2  
Cylinder - body | (10, 0, 200) | 1  
Cube - top face | (10, 10, 255) | 1  
Cube - body | (10, 0, 255) | 1  
Grip | (10, 0, 150) | 1  
  
#### Part 3: ImageSets

This is further separated into 8183 training images and 3474 testing images.

# Code

* * *

You can visit the [_GithubPage_](https://github.com/ChenFengYe/AutoSweep) for
code.  
  

The code consists of two modules, as mentioned in our paper, the learning
module (image to mask) and the graphics module (mask to 3d mesh). The first
module follows the framework of FCIS and Mask RCNN. A common learning
framework with Python. The second module is built based on Unity3D and our own
framework. The purpose of the whole module is to sweep the profiles with a
dynamic demo. I need to remind you that the code is not convenient for a
beginner on 3D. It is really hard to configure this module, I sincerely
suggest you refer to this code only.  
  

The code might no longer be maintained. However, I still hope part of our work
can give you help or inspiration. If you have any questions, please feel free
to ask [ me](http://chenxin.tech).  
  

Code scripts for second module:

AutoSweep_ObjectSnapping/Assets/BodyEngine.cs

AutoSweep_ObjectSnapping/Assets/FaceEngine.cs

AutoSweep_ObjectSnapping/Assets/GraphicsEngine.cs

# Results

* * *

![figure](./WebPage/image/AutoSweep_results.jpg)

# Citation

* * *

Please cite this paper in your publications if it helps your research:

> @article{xin2018autosweep,  
>  title={AutoSweep: Recovering 3D Editable Objects from a Single Photograph},  
>  author={Xin, Chen and Li, Yuwei and Luo, Xi and Shao, Tianjia and Yu,
> Jingyi and Zhou, Kun and Zheng, Youyi},  
>  journal={IEEE transactions on visualization and computer graphics},  
>  year={2018},  
>  publisher={IEEE}  
>  }

# License

* * *

AutoSweep dataset is freely available for free non-commercial use. For
commercial purpose, please email to [ Xin Chen](http://chenxin.tech) or [Youyi
Zheng](http://youyizheng.net).

