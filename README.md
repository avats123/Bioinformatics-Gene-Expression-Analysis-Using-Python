# Bioinformatics Gene Expression Analysis Using Python
Python-based bioinformatics project for preprocessing, analyzing, and visualizing gene expression data.

# Gene Expression Analysis Using Python

## Objective
Analyze gene expression data to identify patterns and differences between biological conditions using a reproducible Python-based workflow.

## Background
Gene expression analysis is a core task in bioinformatics, used to understand how genes are regulated across different biological states such as healthy vs diseased tissue. This project demonstrates a practical data analysis pipeline for processing, analyzing, and visualizing gene expression data using Python.

## Data
The dataset consists of tabular gene expression measurements, where rows represent genes and columns represent samples or experimental conditions.  
Data is stored in TSV format and includes:
- Gene identifiers
- Expression values
- Sample or condition labels

The original dataset is preserved in `data/raw/`, with processed outputs saved to `data/processed/`.

## Methods
The analysis pipeline follows these steps:

1. **Data Loading & Exploration**
   - Loaded gene expression data using `pandas`
   - Inspected structure, summary statistics, and missing values

2. **Preprocessing & Normalization**
   - Removed missing or invalid entries
   - Filtered low-expression genes
   - Applied log-transformation to stabilize variance

3. **Statistical Analysis**
   - Compared gene expression between conditions using statistical tests from `scipy`
   - Computed summary statistics to identify trends

4. **Visualization**
   - Generated histograms and boxplots to visualize expression distributions
   - Saved all figures for reproducibility

## Results
Key outputs of the analysis include:
- Cleaned and normalized gene expression tables
- Statistical summaries comparing conditions
- Visualizations illustrating expression distributions and variability

Figures are saved in `results/figures/`, and summary tables are saved in `results/tables/`.

## Project Structure
```text
gene-expression-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
│   ├── 01_load_and_explore.py
│   ├── 02_preprocessing.py
│   ├── 03_statistics.py
│   └── 04_visualization.py
├── results/
│   ├── figures/
│   └── tables/
├── environment.yml
└── README.md
