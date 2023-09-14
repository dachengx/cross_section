import csv
import numpy as np

from .utils import interp1d_positive, get_file_path


# from http://arxiv.org/abs/1803.09183, FIG.1
with open(get_file_path("es_cross_section.csv"), "r") as f:
    raw = csv.reader(f)
    es_cross_section = np.array([row for row in raw]).astype(float)
es_cross_section = interp1d_positive(es_cross_section[:, 0], es_cross_section[:, 1])
