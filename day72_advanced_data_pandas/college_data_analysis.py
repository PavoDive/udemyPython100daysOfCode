import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")

df.head()

df.shape
# 51 rows and 6 columns

df.columns #output column names

# check the NAs in the data:
df.isna()

# the last row is empty (it contains info about the source of the data)
df.tail()

# remove the last row:
clean_df = df.dropna()

# find the maximum starting salary
max_st_median_salary = clean_df["Starting Median Salary"].idxmax()

clean_df.iloc[max_st_median_salary]

##### Challenges

# What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).
clean_df.iloc[clean_df["Mid-Career 90th Percentile Salary"].idxmax()]

# Which college major has the lowest starting salary and how much do graduates earn after university?
clean_df.iloc[clean_df["Starting Median Salary"].idxmin()]

# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 
clean_df.iloc[clean_df["Mid-Career Median Salary"].idxmin()]

## low risk majors: those with small differences between the lowest and highest salaries:

clean_df.loc[:,"Spread of Salary"] = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]

 # a slightly different approach:
 # spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
 # clean_df.insert(1, "Spread", spread_col)

low_risk = clean_df.sort_values("Spread of Salary")
low_risk[["Undergraduate Major", "Spread of Salary"]].head()

 # Challenges

# Using the .sort_values() method, can you find the degrees with the highest potential? Find the top 5 degrees with the highest values in the 90th percentile.
clean_df.sort_values(by = "Mid-Career 90th Percentile Salary", ascending = False)[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head(n = 5)

# Also, find the degrees with the greatest spread in salaries. Which majors have the largest difference between high and low earners after graduation.
# Here I tried to use a different way of subsetting the data frame
clean_df.sort_values(by = "Spread of Salary", ascending = False).iloc[range(5), [0, 7]]

# Grouping
# which category of degrees has the highest average salary?
clean_df.groupby("Group").count()
clean_df.groupby("Group")[["Starting MEdian Salary", "Spread of Salary"]].median()

