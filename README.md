# Question_Answering
Diploma project based on answering questions using Deep learning.<br>
Scope of the project: Use Deep Learning to answer questions.<br>
**Dataset**: http://jmcauley.ucsd.edu/data/amazon/qa/ <br>
**App link**: In progress <br>

Directory structure:
```
Question_Answering
├── streamlit_app.py     Main file to run the streamlit app_
|── prediction_module.py Prediction module with all the utility functions
├── requirements.txt     Dependencies
├── README.md
├── Model
    ├──final_RFC_FE_model.model  Pickled best RF Model
    ├──tfidf_vec.sav             Pickled TFIDF vectorizer
├── Documentation        Folder for documentation
├── Notebook             Folder for jupyter notebooks
|── data                 Folder for data
```
**NOTE**: _You can ignore the files in the Documentation and Notebook folder._

## How to run in local
Clone the repo using git clone:
```
git clone https://github.com/HrushikeshChaphalkar/Question_Answering  
```
Install dependencies using pip:  
```
pip install -r requirements.txt  
```
Go to CMD and run the following command:  
```
streamlit run streamlit_app.py 
```
(Run it from the root directory of the project).
