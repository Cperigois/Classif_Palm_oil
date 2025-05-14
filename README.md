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

### `run.py`
This is the primary script for executing a full analysis. It should not be modified. The workflow includes:
- **Initialization**: Reads and structures input parameters.
- **Individual detections**: Computes signal-to-noise ratios (SNR) for each binary event.
- **Background computation**: Computes the gravitational wave background spectrum.
- **Data cleaning**: Removes unnecessary temporary files at the end of execution.

### `Run/getting_started.py`
This file is the entry point for setting up a new project. Users must:
- Define the project folder name.
- Specify input astrophysical models.
- Configure detectors and detector networks.
- Set computation parameters.

### `Run/advanced_params.py`
This file contains additional customizable parameters such as:
- Frequency bounds for different detectors.
- Input catalog formatting options.
- Advanced options for background spectrum calculations.

## Usage
To run an analysis, follow these steps:
1. Edit `getting_started.py` with the desired astrophysical models and detector configurations.
2. Run the main script:
   ```bash
   python run.py
   ```
3. The results will be stored in a folder within `Run/`, named after the project.

## Output Structure
After execution, results are stored in `Run/<project_name>/` with the following directories:
- **Astro_Models/**: Contains transformed input catalogs.
- **Results/Analysis/**: Includes SNR values and detection statistics.
- **Results/Omega/**: Contains the gravitational wave background spectrum.
- **Params.json**: Stores all computation parameters for reference.

## Common Issues
- If `Params.json` is not updating, manually delete `Run/Params.json` before re-running.
- Ensure dependencies are installed correctly by running `test.py`.

## Contact
For issues or feature requests, contact the corresponding author or check the GitHub/GitLab repositories.

---
PRINCESS is an evolving tool, and future updates may enhance its capabilities, including new astrophysical models and detector configurations.

