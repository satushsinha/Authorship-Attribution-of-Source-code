**Authorship Attribution of Source code"
Solution for the problem for AI-SOCO contest to predict the author of a programming code.The dataset can be accessed from here https://github.com/AliOsm/AI-SOCO/tree/master/data_dir I create a csv file from this data The code for the same is in Create_Dataset.py file Then using clang library preprocessed the data.Using clang created the abstract syntax tree to tokenize the code then feeded this data to different models tried stacked model too but due to high computation requirements got the best score with random forest model 