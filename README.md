# Raga Generator

## Overview
The Raga Generator is a Python-based project designed to generate new ragas in accordance with Hindustani classical music rules. It utilizes deep learning techniques, specifically Variational Autoencoders (VAEs) or LSTM-based models, to create unique musical compositions by extracting and analyzing musical features from input data.

## Features
- **Musical Feature Extraction**: Extracts notes, rhythm, and ornamentation from input music.
- **Raga Identification**: Identifies the closest matching raga based on extracted features.
- **Raga Generation**: Generates new ragas while adhering to the structural rules of Hindustani classical music.
- **Variations**: Allows for variations in generated ragas while maintaining their validity.

## Project Structure
```
raga-generator
├── src
│   ├── __init__.py
│   ├── vae_raga_generator.py
│   ├── constraints.py
│   ├── models
│   │   ├── __init__.py
│   │   └── vae.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── feature_extraction.py
├── requirements.txt
└── README.md
```

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd raga-generator
pip install -r requirements.txt
```

## Usage
1. Import the necessary modules from the `src` package.
2. Use the `vae_raga_generator.py` to extract features from your input music.
3. The model will identify the closest raga and generate a new raga based on the learned patterns.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.