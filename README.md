# Crime Rate Prediction In California - Group 8 

## Team Members:
- Alexandre Lazzari
- Edward John Tagaca
- Eric Shih
- Hok Yin Cheung
- Marisol Cornejo

## Project Overview:
We aim to develop a machine learning model that predicts crime rates in California based on data from 2010 to 2019. Our hypothesis is that socioeconomic factors such as population, age distribution, income, unemployment rate, house prices, poverty rate, education level, and homeownership have measurable impacts on crime rates. Crime rate is defined as the total number of crimes per 100,000 people.

## Programs Used:
- Python (Pandas, Matplotlib)
- HTML/CSS/Bootstrap
- JavaScript (Plotly)
- Tableau

## Data Sources:
- [Crime Data (Open Justice)](https://openjustice.doj.ca.gov/data)
- [House Price Data (Zillow)](https://www.zillow.com/research/data/)
- [Census Data](https://data.census.gov/)
  - ACS DP02: Education Level
  - ACS DP03: Income and Unemployment Rate
  - ACS DP05: Population and Age
  - B25014: Rent vs. Homeowner
  - S1702: Poverty rate

## Machine Learning Models:
To address our project question, we tested three different machine learning algorithms:
- Multiple Linear Regression
- Random Forest Regression
- Neural Network Algorithm

## Feature and Target Variables:
Our target/dependent variable is crime rate, while our feature/independent variables include:
- % of owner-occupied homes
- % of renter-occupied homes
- Education level
- Average home price
- Age of population
- Income levels
- Unemployment rate
- Total number of crimes

## Data Preprocessing:
Before implementing machine learning models, we performed the following preprocessing steps:
- Imported libraries
- Loaded the final dataset as a CSV file
- Checked for missing values
- Split the dataset into training and testing sets

## Machine Learning Model - Linear Regression:
Linear regression is suitable for predicting numerical outcomes with a linear relationship between features. We utilized multiple linear regression to capture the linear association between crime rate and multiple independent variables. The linear regression model gave us a r-squared value of 0.52 with a accuracy of 51%.

## Machine Learning Model - Random Forest:
Random forest, a supervised learning algorithm, leverages ensemble methods to solve regression and classification tasks. We employed random forest regression to aggregate predictions from multiple decision trees. The random forest model gave us a r-squared value of .72 with a accuracy of 69%.

## Machine Learning Model - Neural Network (More Info):
In addition to linear regression and random forest, we experimented with neural network models, known for their ability to discern intricate patterns. Unlike linear regression, neural networks incorporate hidden layers to enhance prediction accuracy. Using the neural network model to preddict the crime rate based on our data gave us decent results. The neural network showed a r-squared value of 0.80 with an accuracy of 76%. 

## Summary

In our effort to find the best predictor of crime rates in California, we tried out three different machine learning models. To focus our analysis, we narrowed down our dataset by removing certain columns like Crime_Rate_per_100k, City, Violent Crime Sum, City_encoded, and Year, sticking to the most relevant variables.

We started with Linear Regression, a common approach for understanding relationships in data. While it provided some insights, it didn't perform as well as we hoped, with an R-squared value of 0.52 and an accuracy rate of 51%.

Next up was the Random Forest model, which showed more promise with an R-squared value of 0.74 and an accuracy rate of 70%. This model is known for handling complex datasets effectively.

However, the Neural Network model stole the spotlight. Known for its ability to detect intricate patterns in data, it delivered impressive results, boasting an R-squared value of 0.80 and an accuracy rate of 76%. It clearly outperformed both Linear Regression and Random Forest.

Based on these results, it's evident that the Neural Network model is the top choice for predicting future crime rates in California. Its capacity to navigate complex data and capture subtle relationships makes it the most reliable tool for this task.

# Dashboard
We utilized Tableau to create an engaging map of California, featuring cities from our dataset along with their crime rates per 100,000 population. Users can easily filter through the years from 2010 to 2019, witnessing the changes in crime rates over time. This dynamic visualization serves as an introduction, offering a clear picture of which areas experienced the highest levels of crime throughout the nine-year period.
[Link Here](https://public.tableau.com/app/profile/alexandre.lazzari/viz/shared/B37N64Y6J)
