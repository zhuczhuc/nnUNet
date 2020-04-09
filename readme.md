# nnUNet debug version 
# Tested on win10 with Task004_Hippocampus
# In pycharm, you can just run plan.py or run_training.py, then add some breakpoints
# Make sure the Class SingleThreadedAugmenter have next()  method in batchgenerators, if not add this
```python
class SingleThreadedAugmenter(object):
    ...
    def next(self):
        return self.__next__()
```