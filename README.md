# HWR

Download the 
[trained model](https://drive.google.com/file/d/1KJ3dGUlk5nFFY8BQQz8r-8k0BCzpvFDq/view?usp=drive_link)
and place the file "pytorch_model.bin" in the folder "Model".

Use jpg's or png's as input images, place them all in a folder (use the "Input" folder or define your own later)

install the necessary python packages with the following command:
  `pip install -r requirements.txt`

Run the program with python as following:
  `python predict.py <Input directory>`

Or use the predefined input directory:
  `python predict.py Input`
  
The model output will be placed in the "Result" folder, where the output of each seperate image is placed into
a seperate .txt file that has a corresponding name. The inferred text will be placed as a line in this .txt file.

The "Training" folder contains the .ipynb file that was used to train the model on our own dataset. This dataset
is available [here](https://drive.google.com/drive/folders/1110SlSC45GikBDqw-ZZJm22dxpyTCDPg). This dataset is 
created on a subset of the IAM dataset along with a script that was used to augment this data. This script is
located in the "Augment" folder. The training file runs only with the requirements.txt provided in the "Training"
folder.
