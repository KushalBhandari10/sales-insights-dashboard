import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = {
    "Order_ID": range(1, 31),
    "Region": np.random.choice(["East", "West", "Central", "South"], 30),
    "Category": np.random.choice(["Technology", "Furniture", "Office Supplies"], 30),
    "Sales": np.random.randint(100, 2000, 30),
    "Profit": np.random.randint(-200, 800, 30),
    "Discount": np.round(np.random.uniform(0.0, 0.3, 30), 2),
    "Order_Date": pd.date_range(start="2023-01-01", periods=30, freq="D")
}

df = pd.DataFrame(data)
print(df.head())

#Checking null and duplicate value
#from column
print(df.isnull().sum())
#from rows
print(df.duplicated().sum())

total_sales_region = df.groupby("Region")["Sales"].sum()
total_sales_category = df.groupby("Category")["Sales"].sum()
print(total_sales_region)
print(total_sales_category)

sns.histplot(df["Profit"],kde=True)
plt.title("Profit by normal distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

sns.boxplot(df["Profit"])
plt.title("Distribution by boxplot")
plt.show()

corr = df[["Sales","Profit","Discount"]].corr()

import matplotlib.pyplot as plt

# Ensure 'Order_Date' is datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Set it as index
df.set_index('Order_Date', inplace=True)

# Resample and plot monthly sales
monthly_sales = df['Sales'].resample('M').sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(marker='o', linestyle='-')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

Profit = total_sales_category.max()
Name = total_sales_category.idxmax()
print(f"The most profitable category is {Name} with {Profit}")

Q1 = df['Discount'].quantile(0.25)
Q3 = df['Discount'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers
outliers = df[(df['Discount'] < lower_bound) | (df['Discount'] > upper_bound)]
print("Outliers in Discount column:")
print(outliers[['Discount']])
