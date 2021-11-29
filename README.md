# QuMaDe
## Idea
* To propose a new way of dataset generation for depth prediction and foreground mask generation tasks.
![](https://github.com/Lakshman511/QuMaDe/blob/master/Images/teaser.gif)
* Two car datasets:
    1. Synthetic Dataset
    2. Standard dataset
* Two instances of a model
    1. instance1 will be trained on Synthetic dataset
    2. instance2 will be trained on Standard dataset
* Quantitative measures to compare the performance of the two instances of the model
    * Considering threshold accuracies(th1, th2, th3), rmse, absolute relative error, log1o relative error from [here](https://github.com/ialhashim/DenseDepth/blob/master/utils.py)
## Steps to train a model on a dataset
1. [This](https://github.com/Lakshman511/QuMaDe/blob/master/training.ipynb) notebook can be used for training the model.
2. We need to change the constants in the first cell of the above notebook
   * DATA_PATH specifies the path to the folder that contains training images, masks, depth images
   * LIB_PATH specifies the path to [this](https://github.com/Lakshman511/QuMaDe/tree/master/EVALibrary/EVA4) library.
   * Dataset stats (mean, stddev) can be calculated by following [this](https://github.com/Lakshman511/QuMaDe/blob/master/QuMaDe_data_statistics.ipynb) notebook.

## Part1 - Synthetic Dataset
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
  * [These](https://github.com/Lakshman511/QuMaDe/tree/master/Data/bgImages) are 100 background images
  * [These](https://github.com/Lakshman511/QuMaDe/tree/master/Data/fgImages) are 200 foreground images.(100 images are horizontally flipped)
  * [These](https://github.com/Lakshman511/QuMaDe/tree/master/Data/masks) are masks of above foreground images.
  * 400k images are generated as follows..
      ```
      for bg in bgImages: #100 bgImages
        for fg in fgImages: #200 fgImages
          for i in range(multiplexing_factor): #multiplexing_factor = 20
            place_fg_on_bg_randomly(bg,fg)
      # 100*200*20 = 400k
      ```
   * In our dataset generation scale of foreground image, postion on background image are selected randomly.
   * But we can also...
      * Define the range of the scale that each foreground image can have
      * Follow a semantic placement of foreground on background using segmentation maps of background Images.
      
 ## Part2 - Standard Dataset
