-e This file is a merged representation of the entire codebase, combined into a single document

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block or first three lines for files with .csv extensions

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- This file includes only .ipynb and .csv file contents in full or partial form
- All other file types are represented only through the directory structure
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files

# Directory Structure

````
./
fs_report.md
main.py
world_happiness.csv
````
-e 
# Files
-e 
## File: world_happiness.csv
````
Overall rank,Country or region,Score,GDP per capita,Social support,Healthy life expectancy,Freedom to make life choices,Generosity,Perceptions of corruption
1,Finland,7.769,1.340,1.587,0.986,0.596,0.153,0.393
2,Denmark,7.600,1.383,1.573,0.996,0.592,0.252,0.410
````
-e 
## File: main.py
````
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv("world_happiness.csv")
top10 = df.sort_values("Score", ascending=False).head(10)
print(top10)
countries = top10['Country or region'].tolist()
scores = top10['Score'].tolist()
print("Top 10 Countries and Scores:")
for country, score in zip(countries,scores):
    print(f"{country}:{score}")
plt.figure(figsize=(10,6))
plt.bar(countries,scores,color='skyblue')
plt.xticks(rotation = 45, ha = 'right')
plt.xlabel('Country')
plt.ylabel('Hapiness Score')
plt.title('Top 10 Happiest Countries in 2019')
plt.show()
plt.tight_layout()
#Average GDP per capita
missing_count = df['GDP per capita'].isnull().sum()
print(f"Missing values in 'GDP per capita':{missing_count}")
mean_gdp = df['GDP per capita'].mean()
df_imputed = df.copy()
df_imputed['GDP per capita'] = df_imputed['GDP per capita'].fillna(mean_gdp)
top20 = df_imputed.sort_values("Score", ascending = False).head(20) 
bottom20 = df_imputed.sort_values("Score").head(20)
avg_GDP_top20 = top20['GDP per capita'].mean()
avg_GDP_bottom20 = bottom20['GDP per capita'].mean()
print("Average GDP per capita for first 20 countries is:", avg_GDP_top20)
print("Average GDP per capita for bottom 20 countries is:", avg_GDP_bottom20)
missing_score = df['Score'].isnull().sum()
print(f"'Missing values in Score':{missing_score}")
missing_social = df['Social support'].isnull().sum()
print(f"'Missing values in Social support':{missing_social}")
df_clean = df.dropna(subset =['Score','Social support'])
plt.figure(figsize=(8,6))
sns.scatterplot(data = df_clean, x= 'Score', y='Social support',color='red',s=50,edgecolor ='w')
plt.xlabel('Social support')
plt.ylabel('Score')
plt.title('Hapiness Score vs. Social support (2019)')
plt.show()
indicators = ['GDP per capita','Social support','Healthy life expectancy',
              'Freedom to make life choices','Generosity']
correlation = df[indicators].corrwith(df['Score']).sort_values(ascending = False)
print("Correlation of each indicator with Score:")
print(correlation)
top3 = correlation.head(3)
print("Top 3 indicators most correlated with Score:")
print(top3)
#Compare median Healthy life expectancy between two groups
high_score = df[df['Score']>7.0]
low_score = df[df['Score']<5.0]
median_high = high_score['Healthy life expectancy'].median()
median_high = low_score['Healthy life expectancy'].median()

````
