import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('consumer_behavior.csv')
print(data.head())

missing_values = data.isnull().sum()
print(missing_values)

data.dropna(inplace=True)

data['Age'] = data['Age'].astype(int)
data['Purchase Amount'] = data['Purchase Amount'].astype(float)

print(data.describe())

plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], kde=True, bins=30)
plt.title('Age Distribution of Consumers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Purchase Amount'], kde=True, bins=30)
plt.title('Purchase Amount Distribution')
plt.xlabel('Purchase Amount')
plt.ylabel('Frequency')
plt.show()

age_groups = pd.cut(data['Age'], bins=[18, 25, 35, 45, 55, 65, 100], labels=['18-25', '26-35', '36-45', '46-55', '56-65', '65+'])
purchase_by_age_group = data.groupby(age_groups)['Purchase Amount'].mean()
print(purchase_by_age_group)

plt.figure(figsize=(10, 6))
purchase_by_age_group.plot(kind='bar')
plt.title('Average Purchase Amount by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Purchase Amount')
plt.show()

gender_purchase = data.groupby('Gender')['Purchase Amount'].mean()
print(gender_purchase)

plt.figure(figsize=(10, 6))
gender_purchase.plot(kind='bar')
plt.title('Average Purchase Amount by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Purchase Amount')
plt.show()

category_purchase = data.groupby('Product Category')['Purchase Amount'].sum()
print(category_purchase)

plt.figure(figsize=(10, 6))
category_purchase.plot(kind='bar')
plt.title('Total Purchase Amount by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Purchase Amount')
plt.show()
