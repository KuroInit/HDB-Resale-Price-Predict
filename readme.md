# Welcome to HDB Resale Price Prediction Repository

## About

This is a mini-project for SC1015 (Introduction to Data Science and Artifical Intelligence) which focuses on predicting HDB Resale Prices.

For detailed walkthough, review notebooks in the following order:</br>

1. [Data_Prep.ipynb](Data_Prep.ipynb)
2. [Basic_Exploratory_Visualisation.ipynb](Basic_Exploratory_Visualisation.ipynb)
3. [Model_Training.ipynb](Model_Training.ipynb)
4. [Final_Predict.ipynb](FInal_Predict.ipynb)

## Contributors

[@ziyan0117](https://github.com/ziyan0117)

[@KuroInit](https://github.com/KuroInit)

[@thritheman](https://github.com/thritheman)

## Problem Definition

1. Are we able to predict HDB Resale Prices?
2. Which model would be the best?

## Models Used

1. Linear Regression
2. XGBoost
3. Google Tabnet

All models used in this project and saved are available [here](models)

## Conclusion

- XGBoost with log transformation and TabNet are both competitive models in our evaluation.
- XGBoost may appear as the best-performing model initially, but considering computational constraints and data availability, TabNet could surpass XGBoost in predicting resale value given adequate time.
- TabNet adopts a different approach by considering complex interactions between features, unlike traditional models that treat variables independently.
- The importance of a feature in TabNet doesn't solely indicate its standalone significance but rather its role in intricate feature interactions.
- Features with low importance aren't necessarily uninformative; their significance may be context-dependent and emerge through interactions with other features.

## What did we learn?

1. Handling skewed datasets using transformation methods.
2. Neural Networks, Deep Learning and PyTorch.
3. Logistic Regression from sklearn.
4. Other packages such as joblib and json.
5. Collaborating using GitHub.

## Datasets

### For Raw Datasets

You can take it from Data.gov at this [link](https://beta.data.gov.sg/collections/189/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view)

_or_

Head to Data.gov and look for `Resale Flat Prices`

### For Clean Dataset

This repository contains all data both clean and raw inside the [data](data) folder.

## Packages for notebooks

_Recommended to run in virtual environment_

Install all packages

    pip install -r requirements.txt

## References

https://github.com/dreamquark-ai/tabnet
https://arxiv.org/pdf/1908.07442.pdf
https://xgboost.readthedocs.io/en/stable/
