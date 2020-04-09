default_num_threads = 8
RESAMPLING_SEPARATE_Z_ANISO_THRESHOLD = 3  # determines what threshold to use for resampling the low resolution axis
# separately (with NN)

import os
nnUNet_raw_data_base = "./datasets"
nnUNet_preprocessed = "./datasets/preprocess"
RESULTS_FOLDER = "./datasets/trained_models"

os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1, 2, 3'

DEBUG_MODE = True

use_this_for_batch_size_computation_3D = 820000000
MIN_BATCHSIZE = 2
AXIS_2D = None # 0, 1, 2, None->argmax(orignal version)


def set_paths(nnUNet_raw_data_base, nnUNet_preprocessed, RESULTS_FOLDER):
    os.environ['nnUNet_raw_data_base'] = nnUNet_raw_data_base
    os.environ['nnUNet_preprocessed'] = nnUNet_preprocessed
    os.environ['RESULTS_FOLDER'] = RESULTS_FOLDER
set_paths(nnUNet_raw_data_base, nnUNet_preprocessed, RESULTS_FOLDER)
