# croissant-orange-cat-classifier
## About
This classifie uses Python and the knowledge of data science to classify an image between orange cats croissants (yes, sometimes they look alike).
## Table of Contents
* [About](#about)
* [Folders Explained](#folders-explained)
  * [Assets](#assets)
  * [Modules](#modules)
  * [Execution](#execution)
  * [Misc](#misc)
* [Examples](#examples)
* [Installation](#installation)
* [Implementation](#implementation)
* [License](#license)

## Folders Explained
### Assets
This folder includes images used for training and testing. Under this folder, there are two zip files:
* images for croissant (480 in total for data augmentation later)
* images for orange cats (480)

The assets folder also contains a child folder of:
* testing images for classifier to perform predictions and see if the classifier is accurate

### Modules
This folder contains python modules written to help build out reasonable data sets and test if functions and logics work fine. The image_process module contains functions to resize, scale, rotate angles, and add noise, etc. And the cutility module contains a function that count files in a directory.

### Execution
This folder contains a python file that are used to run the classifier.
### Misc
The Misc folder contains assets (pictures,charts,etc.) used to write this readme
## Examples
After model is developed and compiled, run the model and get the following results (30 epochs):

![Image of epochs_beginning](https://github.com/sophieniw/croissant-orange-cat-classifier/blob/master/misc/epoch1.png)

~

![Image of epochs_finish](https://github.com/sophieniw/croissant-orange-cat-classifier/blob/master/misc/epoch2.png)


And below is the plot to show the performance of data training on this model:

![Image of training_graph](https://github.com/sophieniw/croissant-orange-cat-classifier/blob/master/misc/training_graph.png)



The last part of the exec.py provides a way to use the model to predict particular images. I picked 4 pictures that are not used in the model previously to see if my model is accurate. Those 4 pictures are stored under assets/test_img.
The predictions are:

![Image of 
predictions](https://github.com/sophieniw/croissant-orange-cat-classifier/blob/master/misc/predictions.png)


## Installation
* Git clone this repository to your preferred directory 
**or**
* Download this repository
* In the assets folder, there are two zip files. You would need to unzip the files so that you can process the images in the files.

## Implementation
Be aware you would need to change the specific path in the exec.py since we have different working directories and directories to store image sets. To run the model, run the exec.py, and you should see the model start training with 30 epochs. At the end, the program also allows you to plot the training accuracy with respect to epochs.

## License 
Apache License 2.0

