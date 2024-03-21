import pandas as pd

# Sample Data
data = {
    "Category": ["A", "A", "B", "B", "C", "C"],
    "Subcategory": ["X", "Y", "X", "Y", "X", "Y"],
    "Region": ["East", "West", "East", "West", "East", "West"],
    "Value": [10, 20, 30, 40, 50, 60],
}
df = pd.DataFrame(data)

# Set Category, Subcategory, and Region as multi-level indices
df_multi_index = df.set_index(["Category", "Subcategory", "Region"])

# Display DataFrame
# print(df_multi_index)
# print(df_multi_index.loc["A"])
print(df_multi_index.xs("East", level="Region"))
