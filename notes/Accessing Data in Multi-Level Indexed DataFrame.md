---
date: 2024-03-21 12:56
type:
  - evergreen
area:
  - personal
effort:
  - None
---

Suppose this is the code we have to create our multi-index DataFrame:

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

The resulting DataFrame would look like:
```python
                             Value
Category Subcategory Region      
A        X           East       10
         Y           West       20
B        X           East       30
         Y           West       40
C        X           East       50
         Y           West       60
```

To access Category 'A':

```python
print(df_multi_index.loc['A'])

>>
                     Value
Subcategory Region      
X           East       10
Y           West       20
```

To access the 'East' region across all categories and subcategories:

```python
print(df_multi_index.xs('East', level='Region'))

>>
                      Value
Category Subcategory      
A        X               10
B        X               30
C        X               50
```

## List of Functions
- [pandas.DataFrame.set_index](pandas.dataframe.set_index.md)
- [pandas.DataFrame.loc](pandas.dataframe.loc.md)
- [pandas.DataFrame.xs](pandas.dataframe.xs.md)

## Related
- [Pandas DataFrames](pandas-dataframes.md)
- [Indexing and Selecting Data in Pandas DataFrames](indexing-and-selecting-data-in-pandas-dataframes.md)
- [Set MultiIndex with Pandas](set-multiindex-with-pandas.md)

## References
- [pandas.DataFrame.set_index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html)
- [MultiIndex / Advanced Indexing](https://pandas.pydata.org/docs/user_guide/advanced.html

