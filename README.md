<a href="https://www.kaggle.com/code/thierrymasters/salifort-motors-employee-retention-prediction?scriptVersionId=144605639" target="_blank"><img align="left" alt="Kaggle" title="Open in Kaggle" src="https://kaggle.com/static/images/open-in-kaggle.svg"></a>

# Predicting Employee Retention at Salifort Motors: A Machine Learning Approach

## Table of Contents

1. [Project Overview](#project-overview)
2. [Business Understanding](#business-understanding)
3. [Data Understanding](#data-understanding)
4. [Modeling and Evaluation](#modeling-and-evaluation)
5. [Conclusion](#conclusion)


## Project Overview

* **Problem Statement:** This project aims to predict the likelihood of employee attrition at Salifort Motors, a hypothetical automotive company. Employee retention is critical for the long-term success and stability of the business, making it a top priority for HR and management.
* **Data Used:** The dataset used for this project comprises HR records for employees at Salifort Motors, including variables such as age, department, job satisfaction, and years at the company. The dataset contains 15,000 rows and 10 columns for the variables listed below. 

Variable  |Description |
-----|-----|
satisfaction_level|Employee-reported job satisfaction level [0&ndash;1]|
last_evaluation|Score of employee's last performance review [0&ndash;1]|
number_project|Number of projects employee contributes to|
average_monthly_hours|Average number of hours employee worked per month|
time_spend_company|How long the employee has been with the company (years)
Work_accident|Whether or not the employee experienced an accident while at work
left|Whether or not the employee left the company
promotion_last_5years|Whether or not the employee was promoted in the last 5 years
Department|The employee's department
salary|The employee's salary (U.S. dollars)

**source:** For more information about the data, refer to its source on [Kaggle](https://www.kaggle.com/datasets/mfaisalqureshi/hr-analytics-and-job-prediction?select=HR_comma_sep.csv).


* **Key Results:** Utilising machine learning algorithms like Logistic Regression, Decision Trees, and Random Forest, the model achieved notable success with an F1-score of 95.3%, and other metrics like accuracy rate, precision, and recall also showed promising results. The best model overall was the randoom forest model.


## Business Understanding

The success of any organisation heavily relies on the retention of its skilled employees. High turnover rates result in increased recruitment and training costs, leading to a loss of institutional knowledge and decreased overall productivity. In the case of Salifort Motors, understanding the factors contributing to employee attrition is crucial for maintaining a competitive edge in the automotive industry.
For this project, the primary stakeholders are the Human Resources department and the executive leadership team at Salifort Motors. The aim is to develop a predictive model to identify employees at risk of leaving the company, thereby allowing for targeted retention strategies.

## Data Understanding

The dataset used for this analysis is sourced from Salifort Motors' Human Resources department. It contains a comprehensive set of features for each employee, including but not limited to (see table above):

- **Age**: The age of the employee.
- **Department**: The department where the employee works (e.g., Engineering, Sales, HR).
- **Job Satisfaction**: A score indicating the employee's level of job satisfaction.
- **Years at the Company**: The number of years the employee has been with Salifort Motors.

**Data Limitations**: While the dataset is rich in features, it's important to note some limitations. For instance, the dataset lacks information on external factors like industry trends or economic conditions, which could influence employee retention.

**Exploratory Data Analysis (EDA)**: Preliminary data exploration revealed several noteworthy patterns. For example,  some workers quit their jobs due to unsatisfactory management. This decision is influenced by extended working hours, numerous projects, and decreased job contentment. Being overworked without receiving recognition or positive performance reviews can be disheartening. Additionally, a significant number of employees may be experiencing burnout. Interestingly, those who have worked at the company for over six years tend to stay.

![Hours by Project](results/hrs_by_project.png)
*Figure 1: Employees with multiple projects tend to work longer hours. However, two distinct groups of employees left the company - one group worked less than their colleagues with the same number of projects, while the other group worked more.*

For a detailed walkthrough of the data understanding and preprocessing steps, you can visit the following notebooks:

- [Initial EDA and Data Cleaning](notebooks/00_Initial_EDA_and_Data_Cleaning.ipynb)
- [Data Exploration (Continue EDA)](notebooks/01_Data_Exploration_Continue.ipynb)


## Modelling and Evaluation

![Decision Tree Feature Importance](results/dt_feature_imp.png)

*Figure 2: The Decision Tree model has identified certain features such as the `satisfaction_level` and `tenure` as strong predictors.* 


![Random Forest Feature Importance](results/rf_feature_imp.png)

*Figure 3: Features like `satisfaction_level`, `number_project` and `tenure` stand out as significant predictors in the Random Forest model. This suggests that HR policies targeting these areas could have the greatest impact on employee retention.*

![Model Compare](results/model_compare.png)
*Figure 4: The Random Forest model outperforms other models overall. This indicates that it is the most balanced model in terms of precision and recall, making it the recommended model for this project.*


Various machine learning models were employed to tackle the problem of predicting employee attrition at Salifort Motors:

* **Logistic Regression**: Served as the baseline model, achieving an F1-score of 79.9%.
* **Decision Trees**: Provided deeper insights into feature importance, with an F1-score of 94.6%.
* **Random Forest**: Achieved the highest F1-score of 95.3%, making it the preferred model for this project.

***Notebooks for Modeling and Evaluation***

For a detailed understanding of the models and evaluation metrics, you can visit the following Jupyter Notebooks:
- [Logistic Regression](notebooks/02_Logistic_Regression_Model.ipynb)
- [Decision Tree](notebooks/03_Decision_Tree_Model.ipynb)
- [Random Forest](notebooks/04_Random_Forest_Model.ipynb)

**Evaluation Metrics**: The models were evaluated based on several key metrics: accuracy, F1-score, precision, recall and AUC (Area Under the Curve). The Random Forest model excelled across these metrics, confirming its robustness.

**Model Tuning**: To optimise the models further, hyperparameter tuning was performed using GridSearchCV. This step led to a 1.8% improvement in the Random Forest model's F1 score. However, it's AUC decreased by 1.4%.

**Cross-Validation**: To ensure the model's generalisability, a 5-fold cross-validation was conducted, which confirmed the stability of the model's performance.

## Conclusion

The project successfully developed a machine learning model to predict employee attrition at Salifort Motors with an F1-score of 95.3%. The Random Forest model proved to be the most effective, highlighting the importance of features like 'Job Satisfaction', 'Number of Projects' and 'Tenure' in influencing employee retention.

**Recommendations**:

- Implement targeted retention programs focused on employees identified as 'high-risk' by the model.
- Limit the number of projects that employees can work on. 
- Promote employees who have been with the company for at least four years or investigate why these tenured employees are dissatisfied. 
- Stakeholders could either reward employees for working longer hours or limit their hours. 
- Inform employees about the company's overtime pay policies and clarify expectations around workload and time off. Company-wide and within-team discussions can also be held to address work culture. 
- Evaluation scores should be reserved for employees who work less than 200+ hours per month, and a proportionate scale should be used to reward employees who contribute more effort.

**Future Work**:

Expand the dataset to include additional features like employee engagement scores or external economic factors.
Ensemble methods or more complex algorithms like Gradient Boosting or Neural Networks for higher accuracy.