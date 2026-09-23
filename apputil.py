import seaborn as sns
import pandas as pd


# update/add code below ...


# Exercise 1
def fibonacci(n):
    """Returns the nth number of the Fibonacci Series."""
    # only defined for non-negative positions
    if n < 0:
        raise ValueError("n must be a positive integer")

    # the first two numbers of the series are the positions themselves
    if n < 2:
        return n

    # each number is the sum of the previous two
    return fibonacci(n - 1) + fibonacci(n - 2)


# Exercise 2
def to_binary(n):
    """Returns the binary representation of the integer n as a string."""
    # negative numbers: convert the absolute value and add a minus sign
    if n < 0:
        return "-" + to_binary(-n)

    # 0 and 1 are the same in binary as in decimal
    if n < 2:
        return str(n)

    # n // 2 gives every binary digit except the last
    # and the remainder is the last binary digit
    return to_binary(n // 2) + str(n % 2)


# Exercise 3
# load the Bellevue Almshouse Dataset
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)


def _clean_gender(df):
    """Returns a copy of df where invalid gender codes are set to missing."""
    df = df.copy()
    df['gender'] = df['gender'].where(df['gender'].isin(['m', 'w']))
    return df


def task_1():
    """Returns the column names sorted from fewest to most missing values."""

    print("The 'gender' column contains invalid codes ('?', 'g', 'h') that are treated as missing values.")
    df = _clean_gender(df_bellevue)

    # count missing values per column, then sort from least to most
    # (a stable sort keeps the original column order for any ties)
    missing = df.isna().sum().sort_values(kind='stable')

    return missing.index.tolist()


def task_2():
    """Returns a data frame of total admissions for each year."""
    # convert 'date_in' to a datetime in order to pull out the year
    years = pd.to_datetime(df_bellevue['date_in']).dt.year

    # count the number of entries for each year
    df_years = years.value_counts().sort_index().reset_index()
    df_years.columns = ['year', 'total_admissions']

    return df_years


def task_3():
    """Returns a series of the average age for each gender."""

    print("Rows with invalid gender codes are excluded, and rows with a missing age are ignored")
    df = _clean_gender(df_bellevue)

    # group by gender and average the ages
    return df.groupby('gender')['age'].mean()


def task_4():
    """Returns a list of the 5 most common professions"""

    # value_counts sorts from most to least common and ignores missing values
    print("Missing professions are ignored. several of the most "
          "common 'professions' are marital statuses rather than occupations.")
    top_5 = df_bellevue['profession'].value_counts().head(5)

    return top_5.index.tolist()
