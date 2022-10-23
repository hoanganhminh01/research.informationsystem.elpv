# Utilizing Deep Learning Models for Fault Detection and Diagnosis of Photovoltaic Modules - A Case Study
## Abstract
Renewable energy sources have long been considered to be the sole alternatives to fossil fuels. Consequently, the usage of photovoltaic (PV) systems has experienced exponential growth. This growth, however, places gargantuan pressure on the solar energy industry’s manufacturing sector and subsequently begets issues associated with the quality of PV systems, especially the PV module, which is the systems’ most crucial component. Currently, fault detection and diagnosis (FDD) is challenging due to many factors including but not limited to requirements of so-phisticated measurement instruments and experts. Recent advances in deep learning (DL) have proven its feasibility in image classification and object detection. Thus, DL can be extended to visual fault detection using data generated by electro-luminescence (EL) imaging instruments. Here, the authors propose an in-depth approach to exploratory data analysis of EL data and several techniques based on su-pervised and unsupervised learning to detect and diagnose visual faults and defects presented in a module.

**Keywords**: Computer Vision, Supervised Learning, Unsupervised Learning, Deep Learning, Neural Networks.

## Introduction
This code repository is based on a chapter from Information Systems Research in Vietnam Book by Khuong Nguyen-Vinh and Huynh Vo et al. The data used in this study is from Buerhop-Lutz and Deitsch et al. 

## Installation and Setup
### Anaconda
1. Clone the repo.
2. Navigate to the directory containing the cloned repo, then create a virtual environment called `is_elpv` using conda:
```
conda create -n is_elpv
```
3. Activate the recently created environment, then run `requirements.yml` to install all required packages:
```
conda activate is_elpv
conda update -f requirements.yml
```
