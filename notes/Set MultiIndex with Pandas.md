---
date: 2024-03-21 12:14
type:
  - evergreen
area:
  - personal
effort:
  - None
---

When using [pandas](pandas.md), DataFrames by default use an integer-based index. A column from the DataFrame can be used as the index instead, or even multiple columns as a multi-level index. 

There are a few [Benefits of Using MultiIndex DataFrames](benefits-of-using-multiindex-dataframes.md). 

To get the DataFrame into a multi-level index, use the following code:

```python
import pandas as pd

# Sample Data
data = {
	'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
	'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
	'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
	'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Set Category, Subcategory, and Region as multi-level indices
df_multi_index = df.set_index(['Category', 'Subcategory', 'Region'])

# Display DataFrame
print(df_multi_index)
```

- The `set_index` takes a list of the columns that you want to be the new indices and the dataframe will have a hierarchical index structure. 
- By default, `set_index` returns a new dataframe, so you need to assign it to a variable or use the `inplace=True` parameter. 
- If the dataframe you are using is large, to improve performance, it is good practice to sort the DataFrame based on the multi-level indices using the `sort_index` method. 

## List of Functions
- [pandas.DataFrame](pandas.dataframe.md)
- [pandas.DataFrame.set_index](pandas.dataframe.set_index.md)

## Related
- [Pandas DataFrames](pandas-dataframes.md)
- [Indexing and Selecting Data in Pandas DataFrames](indexing-and-selecting-data-in-pandas-dataframes.md)
- [Accessing Data in Multi-Level Indexed DataFrame](accessing-data-in-multi-level-indexed-dataframe.md)

## References
- [pandas.DataFrame.set_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)
- [MultiIndex / Advanced Indexing](https://pandas.pydata.org/docs/user_guide/advanced.html
