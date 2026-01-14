import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

RAW_PATH = "data/raw/GSE68086_TEP_data_matrix.csv"
PROCESSED_DATA = "data/processed/metadata.csv"

def assign_condition_label(colname):
    # assigning biological label for cancer/disease from shorthand notation
    name = colname.lower()
    if "breast" in name:
        return "Breast"
    if "nsclc" in name:
        return "NSCLC"
    if "crc" in name or "colorectal" in name:
        return "CRC"
    if "gbm" in name:
        return "GBM"
    if "pancre" in name:
        return "Pancreatic"
    # fallback: take the first meaningful token
    return "Other"


def main():
    expression_df = pd.read_csv(RAW_PATH)
    # Rename the gene column to Gene ID to standardize
    gene_col = expression_df.columns[0]
    expression_df = df.rename(columns={gene_col: "gene_id"}).set_index("gene_id")
    print(expression_df.head())
    print(expression_df.isnull().sum())
    expression_df.dropna(how="all")
    print(expression_df.head())

main()
