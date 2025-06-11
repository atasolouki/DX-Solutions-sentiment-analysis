# AI Feedback Classifier

## Overview
This project performs sentiment analysis on customer feedback to classify it as Positive or Negative using a pre-trained NLP model from Hugging Face. It includes a Jupyter notebook for analysis and visualization, a dummy dataset, and an optional REST API for on-demand analysis.

## Structure
- `notebook.ipynb`: Jupyter notebook with sentiment analysis and visualization.
- `api.py` (optional): FastAPI script for a sentiment analysis endpoint.
- `dataset.csv`: Dummy dataset with customer feedback.
- `requirements.txt`: List of required Python packages.

## Setup
1. Clone the repository or unzip the project folder.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate