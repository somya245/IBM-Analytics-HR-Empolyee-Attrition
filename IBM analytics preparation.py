import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')
#Loading dataset i the form of CSV file.

employee_data = pd.read_csv(r"C:\Users\Somya\Downloads\WA_Fn-UseC_-HR-Employee-Attrition.csv")
employee_data.head()
employee_data.tail()


#print top 5 data of dataset
print (employee_data.head(5))
#print last 5 data of dataset
print (employee_data.tail(5))



# Print the shape of the DataFrame
print("The shape of data frame:", employee_data.shape)
# Print the length (number of rows) of the DataFrame
print("Number of Rows in the dataframe:", len(employee_data))
# Print the number of columns in the DataFrame
print("Number of Columns in the dataframe:", len(employee_data.columns))

# print enlisted columns in dataset 
print("Column labels in the dataset in column order:")
for column in employee_data.columns:
    print(column)
    
# Check for Non-Null or Nan Nalues in the dataset.
print(employee_data.info(verbose = True))

employee_data.select_dtypes(np.number).sample(5)
employee_data["Education"] = employee_data["Education"].replace({1:"Below College",2:"College",3:"Bachelor",4:"Master",5:"Doctor"})
employee_data["EnvironmentSatisfaction"] = employee_data["EnvironmentSatisfaction"].replace({1:"Low",2:"Medium",3:"High",4:"Very High"})
employee_data["JobInvolvement"] = employee_data["JobInvolvement"].replace({1:"Low",2:"Medium",3:"High",4:"Very High"})
employee_data["JobLevel"] = employee_data["JobLevel"].replace({1:"Entry Level",2:"Junior Level",3:"Mid Level",4:"Senior Level",5:"Executive Level"})
employee_data["JobSatisfaction"] = employee_data["JobSatisfaction"].replace({1:"Low",2:"Medium",3:"High",4:"Very High"})
employee_data["PerformanceRating"] = employee_data["PerformanceRating"].replace({1:"Low",2:"Good",3:"Excellent",4:"Outstanding"})
employee_data["RelationshipSatisfaction"] = employee_data["RelationshipSatisfaction"].replace({1:"Low",2:"Medium",3:"High",4:"Very High"})
employee_data["WorkLifeBalance"] = employee_data["WorkLifeBalance"].replace({1:"Bad",2:"Good",3:"Better",4:"Best"})

#enlisting categorical features
employee_data.select_dtypes(include="O").sample(5).style.set_properties(**{'background-color': '#E9F6E2','color': 'black','border-color': '#8b8c8c'})
# Calculate the number of missing values in each column
    
missing_df = employee_data.isnull().sum().to_frame().rename(columns={0:"Total No. of Missing Values"})
missing_df["% of Missing Values"] = round((missing_df["Total No. of Missing Values"]/len(employee_data))*100,2)
missing_df
# drop unnecessary values
employee_data.describe().T
employee_data.drop(['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'], axis="columns", inplace=True)
# Print top 5 rows in the dataframe.
employee_data.head()
# Print the shape of the DataFrame
print("The shape of data frame:", employee_data.shape)
# Print the length (number of rows) of the DataFrame
print("Number of Rows in the dataframe:", len(employee_data))
# Print the number of columns in the DataFrame
print("Number of Columns in the dataframe:", len(employee_data.columns))
print("Column labels in the dataset in column order:")
for column in employee_data.columns:
    print(column)

#DESCRIPTIVE ANALYSIS ON CATEGORICAL ATTRIBUTES
employee_data.describe(include="O").T
# Calculate the number of unique values in each column
for column in employee_data.columns:
    print(f"{column} - Number of unique values : {employee_data[column].nunique()}")
    print("=============================================================")
categorical_features = []
for column in employee_data.columns:
    if employee_data[column].dtype == object and len(employee_data[column].unique()) <= 30:
        categorical_features.append(column)
        print(f"{column} : {employee_data[column].unique()}")
        print(employee_data[column].value_counts())
        print("====================================================================================")
categorical_features.remove('Attrition')
# Calculate the number of unique values in each column
for column in employee_data.columns:
    print(f"{column} - Number of unique values : {employee_data[column].nunique()}")
    print("=============================================================")
# Save DataFrame to CSV file
employee_data.to_csv(r"C:\Users\Somya\Downloads\WA_Fn-UseC_-HR-Employee-Attrition.csv", index=False)


