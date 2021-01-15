# Pixel wise Breast Mammography Image Segmentation using Generative Adversarial Networks
This repository contains code for SegNet-cGAN and UNET-cGAN for Breast Mammography Segmentation and also a discussion of the results we were able to achieve with our implementation.

## Explanations:
This repo is originated from [GAN_breast_mammography_segmentation](https://github.com/ankit-ai/GAN_breast_mammography_segmentation)

### Modificatoin:
1. Did not use CBIS-DDSM as the original repo. Instead, using INbreast(http://medicalresearch.inescporto.pt/breastresearch/index.php/Get_INbreast_Database) as dataset. You need to access to it by signing an Agreement. 
2. Some codes in the original main.py file were anotated however they were essential to make it. Little changes in the main.py file.

### Training Process:
102 pairs of mammography and mask images were obtained from INbreast dataset. Since it is not enough, I used Keras ImageDataGenerator to get 20052 images to train. Something needed to be noticed: the code in the main.py requires the number of training images minus 4 to be the multiple of batch number(which is 8 in the default setting). For example, (20052 - 4) % 8 = 0. You can find it in line 232.

### Testing Process:
Using python main.py --mode=evaluate to have a test. The output of test results are stored in /sample/evaluate. 

Some samples of the training/testing images are also uploaed in train_data_in/train_data_out/test_data_in/test_data_out

The following are the original README file.
**************************************************************************
## Contributors:
Ankit Chadha (ankitrc@stanford.edu) and Rewa Sood (rrsood@stanford.edu)
This work is an extension of the work we had done for CS229.

![GAN for breast mammography](https://github.com/ankit-ai/GAN_breast_mammography_segmentation/blob/master/images/Screen%20Shot%202019-01-06%20at%209.47.40%20PM.png)


## Dataset and Augmentation
The dataset we used was CBIS-DDSM [3]
The DDSM is a database of 2,620 scanned film mammography studies.
Since our problem is becomes challenging with very limited number of samples, we resorted to data augmentation without changing underlying pathology information of the image. 

Techniques used for augmentation were:
1. Image Rotation (90 degrees)
2. Image Flipping
3. Tissue Augmentation [1]

## Architecture:
The above poster shows results for training the UNet without adversarial training. We extended the UNet and SegNet with adversarial training to generate more precise masks.

![GAN for breast mammography](https://github.com/ankit-ai/GAN_breast_mammography_segmentation/blob/master/images/Screen%20Shot%202019-01-06%20at%2010.10.34%20PM.png)
[2] Presents recent work where cGAN implementations were used for mammography segmentation

1. U-Net Architecture [4]
![U-Net with cGAN](https://github.com/ankit-ai/GAN_breast_mammography_segmentation/blob/master/images/unet.jpg)
2. SegNet Architecture [5]
![SegNet with cGAN](https://github.com/ankit-ai/GAN_breast_mammography_segmentation/blob/master/images/Screen%20Shot%202019-01-06%20at%2010.24.55%20PM.png)

## Code Description and Configuration
```You can run the model and the harness around it using:
python main.py

Run evaluate over your test set
python main.py --mode=evaluate

Configuration: config.py 

config.TRAIN.batch_size = 8 #Training batch size

config.TRAIN.lr_init = 1e-4 #Initial Learning Rate

config.TRAIN.beta1 = 0.9 #Beta1 parameter for batch normalization

config.TRAIN.n_epoch_init = 35 #Number of epochs to run the generator before adversarial training

config.TRAIN.n_epoch = 56 #Number of Epochs of Adversarial training
config.TRAIN.lr_decay = 0.1 #Learning rate decay through adversarial training
config.TRAIN.decay_every = int(config.TRAIN.n_epoch / 2) 

config.TRAIN.hr_img_path = '../train_data_out_2'
config.TRAIN.lr_img_path = '../train_data_in'

config.VALID.hr_img_path = '../test_data_out_2/'
config.VALID.lr_img_path = '../test_data_in/'
```

TRAIN.hr_img_path is the groundtruth path and TRAIN.lr_img_path is the input image path. In our case these are 128x128 slices of input image and binary masks.

## Results
| Model        | Dice           | model filename  |
| ------------- |:-------------:| -----:|
| SegNet-cGAN      | 89% | model_vae.py |
| Unet-cGAN      | 86.3%      |   unet_tf.py |

## Sample outputs
-- Network output and Ground truth
1.
### Groundtruth:
![sample1](https://github.com/ankit-ai/GAN_breast_mammography_segmentation/blob/master/images/Screen%20Shot%202019-01-06%20at%2010.38.16%20PM.png)
### Network output:
![sample1](https://github.com/ankit-ai/GAN_breast_mammography_segmentation/blob/master/images/Screen%20Shot%202019-01-06%20at%2010.38.23%20PM.png)

2.
### Groundtruth:
![sample2](https://github.com/ankit-ai/GAN_breast_mammography_segmentation/blob/master/images/Screen%20Shot%202019-01-06%20at%2010.38.43%20PM.png)
### Network output:
![sample2](https://github.com/ankit-ai/GAN_breast_mammography_segmentation/blob/master/images/Screen%20Shot%202019-01-06%20at%2010.38.54%20PM.png)

Post-processing techniques used: Otsu Thresholding, Opening and Major component selection to denoise the network output

## References
[1] Tisse Augmentation - https://www.ncbi.nlm.nih.gov/pubmed/28094850

[2] Conditional Generative Adversarial and Convolutional Networks for X-ray Breast Mass Segmentation and Shape Classification - https://arxiv.org/pdf/1805.10207.pdf

[3] CBIS-DDSM Dataset https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM

[4] U-Net https://arxiv.org/pdf/1505.04597.pdf

[5] SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation - https://arxiv.org/pdf/1511.00561.pdf
