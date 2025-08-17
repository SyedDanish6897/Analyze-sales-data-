import pandas as pd
import matplotlib.pyplot as plt

# for reading dataset
df=pd.read_csv("sales_data.csv")

#  for showing fist few rows 
print("Samle Data: ")
print(df.head())

# for basic info
print("\nData info")
print(df.info())

sales_by_product = df.groupby("Product")["Sales"].sum()
print("\n Sales By Product: ")
print(sales_by_product)

sales_by_region = df.groupby("Region")["Sales"].sum()
print("\n Sales By Region: ")
print(sales_by_region)
# For Visualization
sales_by_product.plot(kind="bar", title="Sales By Product", figsize=(5,4))
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()


sales_by_region.plot(kind="pie", autopct= "%1.1f%%" ,title="Sales By region", figsize=(6,4))

plt.ylabel("")
plt.show()