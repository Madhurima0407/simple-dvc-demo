# load the train and test
# train algo
# save the metrices, params
import os
import sys
import warnings
import pandas as pd
import numpy as np
import json
import joblib
import argparse
from get_data import read_params
from urllib.parse import urlparse
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet