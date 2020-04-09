# -*- coding:utf-8 -*-
import os
import shutil

def maybe_mkdir_p(path):
    """
    Creates a folder at the given path if one doesnt exist before
    ===

    :param path: destination to check for existense
    :return: None
    """
    if not os.path.exists(path):
        os.makedirs(path)
    # else:
    #     shutil.rmtree(path)
    #     os.mkdir(path)