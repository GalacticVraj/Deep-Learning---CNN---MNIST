# Deep-Learning---CNN---MNIST

# Deep Learning CNN MNIST

This project implements a Convolutional Neural Network (CNN) to classify handwritten digit images from the MNIST dataset. The MNIST dataset consists of 28x28 grayscale images of digits from 0 to 9.

## Overview
The CNN model is designed to learn features from the images to effectively predict the digit class. This implementation provides an end-to-end pipeline, including data loading, model building, training, and evaluation.

## Features
- CNN architecture tailored for the MNIST digit recognition task
- Training on the MNIST dataset
- Model evaluation with accuracy metrics

## Repository Contents
- `app.py`: Main application file to run the model
- `model.h5`: Pre-trained model weights file
- `dl.ipynb`: Jupyter notebook for model development and experimentation
- `templates/`: Directory potentially containing HTML templates (if applicable)
- `static/`: Directory potentially containing static assets

## Getting Started
### Prerequisites
- Python 3.x
- TensorFlow and Keras
- Jupyter Notebook (optional, for running dl.ipynb)

### Installation
1. Clone the repository:
    ```
    git clone https://github.com/GalacticVraj/Deep-Learning-CNN-MNIST.git
    cd Deep-Learning-CNN-MNIST
    ```
2. Install required packages:
    ```
    pip install tensorflow numpy matplotlib
    ```

### Running the Model
- To run the model training and evaluation, open and execute the Jupyter notebook `dl.ipynb`.
- Alternatively, run the application script `app.py` if it contains standalone code to perform training or inference.

## Usage
- Train the CNN model on MNIST dataset
- Evaluate model accuracy on test data
- Save and load trained model weights

## Author
- GalacticVraj

[1] https://github.com/GalacticVraj/Deep-Learning-CNN-MNIST
