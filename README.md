**Authorship Attribution of Source code**
Here is a solution to the problem for the AI-SOCO contest to predict the creator of the programming ordinance. The dataset can be accessed from here https://github.com/AliOsm/AI-SOCO/tree/master/data_dir.

A CSV file is concocted by me from this data. The code for the equivalent is in the Create_Dataset.py file.

Furthermore using the clang library, the data is preprocessed. Exploiting clang, I created the abstract syntax tree to tokenize the code then sustained this data to different prototypes and likewise attempted the stacked model but due to high computation requirements reaped the best tally with the random forest model.
