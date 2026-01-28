📉 Customer Churn Prediction Project

📌 Objective :
Build an end-to-end Customer Churn Prediction system to identify customers who are likely to leave a service, using machine learning and data-driven insights.

This project focuses on:
•	Understanding customer behavior through EDA
•	Creating meaningful features to capture churn patterns
•	Training and comparing multiple ML models
•	Optimizing decision thresholds for business impact

📊 Dataset

•	Dataset used: data/raw/Customer churn data.csv
•	The dataset contains 10,000 customer records with the following information:
•	Customer demographics (Age, Gender, Country)
•	Financial attributes (Credit score, Balance, Salary)
•	Product & engagement data (Tenure, Products, Credit card, Active member)
•	Target variable: churn
•	0 → Customer stays
•	1 → Customer churns

🛠️ Libraries Used

1.	Python
2.	NumPy
3.	Pandas
4.	Matplotlib
5.	Seaborn
6.	Scikit-learn
7.	Jupyter Notebook

📈 Exploratory Data Analysis (EDA)

EDA was performed to understand how different factors influence customer churn.
Key visualizations include:
	Distribution of numerical features by churn status
	Pairwise relationships between financial variables
	Age distribution and tenure analysis
	Gender, country, and product-based churn comparison
	Correlation heatmap
	Balance vs number of products analysis
	All visualizations are saved in the reports/ folder.

🧠 Feature Engineering

Custom features were created to better capture customer behavior:
1.	Balance per product
2.	Zero balance indicator
3.	Salary to balance ratio
4.	Customer engagement flag
5.	Age groups
6.	Tenure groups
7.	Product usage category
8.	Credit score bands
These features improved both model performance and interpretability.

⚙️ Data Preprocessing

A clean and reusable preprocessing pipeline was built using ColumnTransformer:
•	Numerical Features
•	Missing value imputation (median)
•	Standard scaling
•	Categorical Features
•	Missing value imputation (most frequent)
•	One-hot encoding

🤖 Models Trained

The following models were trained and evaluated using the same preprocessing pipeline:

1.	Logistic Regression
2.	Random Forest Classifier
3.	Gradient Boosting Classifier

🎯 Model Evaluation Strategy

Models were evaluated using:

•	Accuracy
•	Precision
•	Recall
•	F1-Score
•	ROC-AUC
•	Confusion Matrix

Since churn prediction is a business-critical problem, recall for churners was prioritized.

🎚️ Threshold Optimization

Instead of relying on the default 0.5 probability threshold, multiple thresholds were tested:

	0.50
	0.40
	0.35
	0.30 (best trade-off)

Lowering the threshold significantly improved recall, ensuring fewer churners were missed.

🏆 Final Model & Results
✅ Final Model: Gradient Boosting Classifier
Optimal Threshold: 0.30

Performance Highlights:

	High recall for churned customers
	Balanced precision and F1-score
	ROC-AUC ≈ 0.87, indicating strong class separation

This model provides the best balance between business needs and predictive performance.

📌 Key Insights (Summary)

•	Customers with low tenure and low engagement are more likely to churn
•	Zero-balance customers show a higher churn tendency
•	Customers with multiple products are generally more stable
•	Credit score and age play an important role in churn behavior
•	Adjusting the probability threshold improves business-oriented outcomes

🚀 Future Improvements

•	Hyperparameter tuning using GridSearchCV
•	Advanced models like XGBoost or LightGBM
•	Model explainability using SHAP
•	Deployment as a REST API using Flask/FastAPI

