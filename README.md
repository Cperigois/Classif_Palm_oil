# Classification of Palm Oil Satellite Images

_**Classif_Palm_oil**_ is a small project aimed at becoming familiar with the classification of satellite images using PyTorch.  
The goal is to classify images based on the presence or absence of palm oil plantations.

This project was originally proposed on Kaggle, and the original dataset and publication can be found at the following link:  
[https://www.kaggle.com/competitions/widsdatathon2019/data](https://www.kaggle.com/competitions/widsdatathon2019/data)

The project is developed by Carole Périgois ([carolperigois@outlook.com](mailto:carolperigois@outlook.com)) and was chosen for its environmental and humanitarian relevance.

---

## Overview

This project explores the classification of satellite images using deep learning techniques, with a focus on detecting palm oil plantations. Palm oil production has a significant impact on the environment, contributing to deforestation and habitat loss. By automating the detection of such plantations, we can contribute to large-scale monitoring tools for environmental impact assessments.

The dataset comes from the WiDS Datathon 2019 on Kaggle and includes labeled satellite images from various geographical locations. The project aims to:

- Preprocess and visualize satellite imagery
- Build and train a convolutional neural network using PyTorch
- Evaluate model performance using appropriate metrics
- Investigate generalization to unseen data

While the scope is currently exploratory and educational, the methodology can be extended to other remote sensing classification tasks.

---

## Installation and Requirements

See `pyproject.toml` for details on dependencies and installation instructions.

---

## Repository Structure
```
Classif_Palm_oil/
│-- docs/ # Sphinx documentation source files
│-- Raw_kaggle_data/ # Original data from Kaggle (described in a dedicated section)
│-- src/
│ ├── Classif_Palm_oil/
│ │ ├── init.py # Initial parameter configuration
│ ├── run.py # Main script executing the full analysis
│-- pyproject.toml
│-- README.md
│-- readthedocs.yaml
│-- setup.py
```

## Main Code Files

