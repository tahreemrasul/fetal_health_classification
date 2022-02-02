# fetal_health_classification
The data set can be viewed on Kaggle: 
https://www.kaggle.com/andrewmvd/fetal-health-classification 

# Dataset
Reduction of child mortality is reflected in several of the United Nations' Sustainable Development Goals and is a key indicator of human progress.
The UN expects that by 2030, countries end preventable deaths of newborns and children under 5 years of age, with all countries aiming to reduce under‑5 mortality to at least as low as 25 per 1,000 live births. Parallel to notion of child mortality is of course maternal mortality, which accounts for 295 000 deaths during and following pregnancy and childbirth (as of 2017). The vast majority of these deaths (94%) occurred in low-resource settings, and most could have been prevented. In light of what was mentioned above, Cardiotocograms (CTGs) are a simple and cost accessible option to assess fetal health, allowing healthcare professionals to take action in order to prevent child and maternal mortality. The equipment itself works by sending ultrasound pulses and reading its response, thus shedding light on fetal heart rate (FHR), fetal movements, uterine contractions and more.[1]

This dataset contains 2126 records of features extracted from Cardiotocogram exams, which were then classified by three expert obstetritians into 3 classes:
- Normal
- Suspect
- Pathological

The data preprocessing and analysis is present in the jupyter notebook "fetal classification.ipynb"

# Data Preprocessing and Analysis
1) Each feature is explored using unique values.
2) Missing values are dealt with
3) Correlation analysis is performed using seaborn and matplotlib libraries
4) Data is divided into independent and dependent features
5) An ExtraTreesClassifier is used to fit the model, and the feature_importances_ attribute of the model is used to visualize the top features (a bar graph is plotted)
6) The top features are used to create a new dataframe

# Train Test Split and Model Creation
1) Using sklearn's train_test_split, the data is divided into training and test data. 80% of the data is used for training
2) A Random Forest Classifier is used to fit the dataset. 

# Hyperparameter tuning
1) Important parameters of the training dataset are initialized at random. These include: no. of trees in forest, maximum depth of tree, number of features considered at each split, minimum samples required for split and the minimum samples required at a leaf node. 
2) A base estimator is created (Random Forest Classifier)  and using the randomly initialized hyperparameter values, a grid search is employed to find the best values of these hyperparamaters. The scoring is performed based on the accuracy metric. 
3) The best parameters can be seen using the best_params_ attribute post model fitting

# Evaluation Metrics
1) The accuracy metric is evaluated. The model gives an accuracy of 94%
2) A confusion matrix is calculated to visualize the true positive and true negative rate of each class. These are high for all classes. and the false positive rates are pretty low.

# Saving the model
The model is then saved. It is now ready to be deployed as an app.

# Model deployment
The Flask framework is employed in the file "app.py" to deploy the framework as a webpage. Values of important parameters are asked from the user, and given to the saved model to be predicted. 
The HTML and CSS code is present in templates/index.html
The model is deployed in the Heroku cloud platform, and can be viewed at the following link: https://fetalhealthclassifier.herokuapp.com/. The app asks for values of certain features, and predicts the fetal health using the deployed model. 

# References
[1] Ayres de Campos et al. (2000) SisPorto 2.0 A Program for Automated Analysis of Cardiotocograms. J Matern Fetal Med 5:311-318
