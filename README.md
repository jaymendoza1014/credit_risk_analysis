# Loan Approval Calculator
## Overview
This repository contains a Loan Approval Calculator application and supporting Jupyter notebook for data analysis and model creation. The app predicts whether a loan will be approved or denied based on user-provided data, leveraging a logistic regression model.

## Repository Contents
- loan_calculator.py: Streamlit application for loan approval predictions.
- credit_risk_evaluation_model.ipynb: Jupyter notebook containing exploratory data analysis (EDA), data cleaning, and model creation.
- requirements.txt: Required libraries
- credit_application_lg_model.pkl: Logistic Regression Model created in credit_risk_evaluation_model.ipynb
- credit_application_scaler.pkl: Scaler for model 

## Prerequisites
Python 3.8 or higher
Required libraries (listed in requirements.txt)

## Running the Application:
Visit the app at: https://creditriskanalysis-loanapplication.streamlit.app/ 


## Inputs and Outputs
App Inputs:
1. Age
2. Annual income
3. Home ownership
4. Employment length
5. Loan purpose
6. Requested loan amount
7. Loan default history
8. Credit history length

App Outputs:
- Loan Approved: Indicates approval of the loan.
- Loan Denied: Indicates denial of the loan.

## Acknowledgments
- Datasets: Open-source datasets from Kaggle.
- Libraries: Streamlit, Scikit-learn, Pandas, NumPy.
