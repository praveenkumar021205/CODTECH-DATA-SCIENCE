# Task 2: Deep Learning Image Classification

*Domain:* Computer Vision / Deep Learning  
*Technique:* Convolutional Neural Networks (CNN)  
*Dataset:* CIFAR-10  

## Description
This project implements a Deep Learning model to classify images into 10 distinct categories using the CIFAR-10 dataset. The model is built using *TensorFlow/Keras* and utilizes Convolutional Neural Networks (CNN) to extract features and classify images with high accuracy.

## The Problem
Image classification is a fundamental task in computer vision where the goal is to categorize an image into a specific class. This project solves the problem of distinguishing between 10 different objects (Airplanes, Cars, Birds, Cats, Deer, Dogs, Frogs, Horses, Ships, and Trucks) automatically.

## Methodology
1.  *Data Loading:* Utilized the CIFAR-10 dataset containing 60,000 32x32 color images.
2.  *Preprocessing:* Normalized pixel values to the range [0, 1] for faster convergence.
3.  *Model Architecture:* * 3 Convolutional Layers (Conv2D) with ReLU activation.
    * 2 Max Pooling Layers (MaxPooling2D) to reduce spatial dimensions.
    * Dense Layers for final classification.
4.  *Training:* Compiled with Adam optimizer and SparseCategoricalCrossentropy loss function.
5.  *Evaluation:* Visualized training accuracy vs. validation accuracy to check for overfitting.

## Libraries Used
* *TensorFlow / Keras:* For building and training the neural network.
* *Matplotlib:* For visualizing the images and plotting accuracy graphs.
* *NumPy:* For numerical operations.

## Results
The model successfully classifies images with a reasonable accuracy, demonstrating the effectiveness of CNNs in extracting spatial hierarchies from image data.
