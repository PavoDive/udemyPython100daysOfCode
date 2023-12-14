import pandas as pd
import matplotlib.pyplot as plt

programming_languages = pd.read_csv("QueryResults.csv", names = ["date", "tag", "posts"], header = 0)

programming_languages.head()
programming_languages.tail()

programming_languages.shape

programming_languages.count() # non-na values in each column

# The TAG is the name of the programming language. So for example in July 2008, there were 3 posts tagged with the language C#. Given that the TAG serves as our category column, can you figure out how to count the number of posts per language? Which programming language had the most number of posts since the creation of Stack Overflow? (Hint: you may need to review one of yesterday's lessons).

programming_languages.groupby("tag")["posts"].sum().sort_values(ascending = False)

# Also, some languages are older like C and other languages are newer (like Swift). The dataset starts in July 2008, so some languages will not have any posts for every month. Can you count how many months of posts exist for each programming language?

programming_languages.groupby("tag")["date"].count()

# inspecting the data type
type(programming_languages["date"][1])

# convert to date
programming_languages.date = pd.to_datetime(programming_languages.date)

# convert long to wide:
wide_df = programming_languages.pivot_table(index = "date", columns = "tag", values = "posts", fill_value = 0)

# plot java
# columns need to be converted to numpy to avoid an error
plt.plot(wide_df.index.to_numpy(), wide_df.java.to_numpy())
plt.show()

# plotting two lines:
plt.plot(wide_df.index.to_numpy(), wide_df.python.to_numpy(), label = "Python")
plt.plot(wide_df.index.to_numpy(), wide_df.r.to_numpy(), label = "R")
plt.legend()
plt.xlabel("Date")
plt.ylabel("Number of posts")
plt.show()

# rolling mean
roll_df = wide_df.rolling(window = 6).mean()

plt.xlabel("Date")
plt.ylabel("Number of posts")

for column in roll_df.columns:
    plt.plot(roll_df.index.to_numpy(), roll_df[column].to_numpy(), label = roll_df[column].name)

plt.legend()
plt.show()

#### questions

# most popular language from 2008 to 2012
mask = (programming_languages.date >= "2008-01-01") & (programming_languages.date <= "2012-12-01")
programming_languages.loc[mask].groupby("tag").posts.sum().sort_values(ascending = False).index[0]

# most popular language from 2015 to 2018
mask = (programming_languages.date >= "2015-01-01") & (programming_languages.date <= "2018-12-01")
programming_languages.loc[mask].groupby("tag").posts.sum().sort_values(ascending = False).index[0]

# most popular language in 2020
mask = (programming_languages.date >= "2020-01-01") & (programming_languages.date <= "2020-12-01")
programming_languages.loc[mask].groupby("tag").posts.sum().sort_values(ascending = False).index[0]
