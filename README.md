# Predicting Employee Retention at Salifort Motors: A Machine Learning Approach

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