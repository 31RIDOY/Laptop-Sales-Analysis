# LIBRARIES IMPORT

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# DATA LOAD

df = pd.read_csv("laptop_sales.csv")


# AVERAGE PRICE BY BRAND (BAR PLOT)

# avg_price = df.groupby("Company")["Price"].mean().sort_values(ascending=False)
# print(avg_price)

# plt.figure(figsize=(10,8))
# sns.barplot(x=avg_price.index, y=avg_price.values, palette="magma")
# plt.title("Average Price by Brand")
# plt.ylabel("Average Price")
# plt.tight_layout()
# plt.show()


# COUNT OF LAPTOP TYPES (COUNT PLOT)


# plt.figure(figsize=(10,8))
# sns.countplot(data=df, x="TypeName", color="g")
# plt.title("Distribution of Laptop Types")
# plt.xlabel("Types of Laptop")
# plt.ylabel("")
# plt.tight_layout()
# plt.show()


# RAM VS PRICE (BAR PLOT)

# ram_list = sorted(df["Ram"].unique(), key= lambda x: int (x.replace("GB","")))
# print(ram_list)
# plt.figure(figsize=(10,8))
# sns.barplot(data=df, x="Ram", y="Price",order=ram_list, color="g")
# plt.title("Relationship between Ram & Price")
# plt.tight_layout()
# plt.show()


# OPERATING SYSTEM VS PRICE

# opsys = df.groupby("OpSys")["Price"].mean().sort_values(ascending=False)
# # print(opsys)
# plt.figure(figsize=(10,8))
# sns.barplot(x=opsys.index, y= opsys.values)
# plt.title("Relationship between Operating System & Price")
# plt.xlabel("Operating System")
# plt.ylabel("Average Price")
# plt.tight_layout()
# plt.show()


# WEIGHT VS PRICE

# df["Weight"] = df["Weight"].str.replace("kg","").astype(float)

# plt.figure(figsize=(10,8))
# sns.scatterplot(data=df, x="Weight", y="Price")
# plt.title("Relationship between Weight & Price")
# plt.xlabel("Weight(KG)")
# plt.tight_layout()
# plt.show()