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
median_low = low_score['Healthy life expectancy'].median()
print(f"'Median Healthy life expectancy for Score above 7.0':{median_high}")
print(f"'Median Healthy life expectancy for Score below 5.0':{median_low}")

