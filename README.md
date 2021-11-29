# QuMaDe
* Sample files to train a model for predicting mask as well as depth images on a dataset.
* .ipynb notebooks are used for traininng instead of training in the terminal because itcan be interactive. 
### Steps to train a model on a dataset
1. [This](https://github.com/Lakshman511/QuMaDe/blob/master/training.ipynb) notebook can be used for training the model.
2. We need to change the constants in the first cell of the above notebook
   * DATA_PATH specifies the path to the folder that contains training images, masks, depth images
   * LIB_PATH specifies the path to [this](https://github.com/Lakshman511/QuMaDe/tree/master/EVALibrary/EVA4) library.
   * Dataset stats (mean, stddev) can be calculated by following [this](https://github.com/Lakshman511/QuMaDe/blob/master/QuMaDe_data_statistics.ipynb) notebook.


### Data
```
|---DATA_PATH
    |---depth                  # contains 400k depth images
        |---img000001.jpg
        |---img000002.jpg
        |---img000003.jpg
        ....
    |---images                # contains 400k RGB images corresponding to the above depth images
        |---img000001.jpg
        |---img000002.jpg
        |---img000003.jpg
        ....
    |---masks                 # contains 400k masks for the above RGB images
        |---img000001.jpg
        |---img000002.jpg
        |---img000003.jpg
        ....
```
