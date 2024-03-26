import pandas as pd
import numpy as np
import pdb
import csv


class UniqueSvs:
    def __init__(self, file: str) -> None:
        self.dataframe = pd.read_csv(file, sep="\t")
        pass
