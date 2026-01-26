import numpy as np
import pandas as pd


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
   

    df = df.copy()

    # 1️⃣ Balance per product
    df['balance_per_product'] = (
        df['balance'] / df['products_number'].replace(0, np.nan)
    )
    df['balance_per_product'] = df['balance_per_product'].fillna(0)

    # 2️⃣ Zero balance flag
    df['zero_balance'] = (df['balance'] == 0).astype(int)

    # 3️⃣ Salary to balance ratio
    df['salary_balance_ratio'] = (
        df['estimated_salary'] / df['balance'].replace(0, np.nan)
    )
    df['salary_balance_ratio'] = df['salary_balance_ratio'].fillna(0)

    # 4️⃣ Engagement feature
    df['engaged_customer'] = (
        (df['credit_card'] == 1) &
        (df['active_member'] == 1)
    ).astype(int)

    # 5️⃣ Age group
    df['age_group'] = pd.cut(
        df['age'],
        bins=[18, 30, 45, 60, 100],
        labels=['Young', 'Mid-age', 'Senior', 'Old']
    )

    # 6️⃣ Tenure group
    df['tenure_group'] = pd.cut(
        df['tenure'],
        bins=[0, 2, 5, 10],
        labels=['New', 'Medium', 'Old']
    )

    # 7️⃣ Product category
    df['product_category'] = pd.cut(
        df['products_number'],
        bins=[0, 1, 2, 4],
        labels=['Low', 'Medium', 'High']
    )

    # 8️⃣ Credit score band
    df['credit_score_band'] = pd.cut(
        df['credit_score'],
        bins=[300, 580, 670, 740, 850],
        labels=['Poor', 'Fair', 'Good', 'Very Good']
    )

    return df

