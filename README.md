# HWR

Tested python version: 3.10.12,3.9.16,3.8.16



install the necessary python packages with the following command:
  `pip install -r requirements.txt`

Use jpg's or png's as input images, place them all in a folder (use the "Input" folder or define your own later)


Run the program with python as following:
  `python predict.py <Input directory>`

Or use the predefined input directory:
  `python predict.py Input`

The model output will be placed in the "result" folder, where the output of each seperate image is placed into
a seperate .txt file that has a corresponding name. The inferred text
will be placed as a line in this .txt file. (Note: the files name ends
with _characters if you desire another suffix please change the
variable `NAMING` in the `predict.py` file.)



The "Training" folder contains the .ipynb file that was used to train the model on our own dataset. This dataset
is available [here](https://drive.google.com/drive/folders/1110SlSC45GikBDqw-ZZJm22dxpyTCDPg). This dataset is
created on a subset of the IAM dataset along with a script that was used to augment this data. This script is
located in the "Augment" folder. The training file runs only with the requirements.txt provided in the "Training"
folder.
