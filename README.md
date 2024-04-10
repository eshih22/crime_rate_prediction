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

## Data Preprocessing (More Info):
Before implementing machine learning models, we performed the following preprocessing steps:
- Imported libraries
- Loaded the final dataset as a CSV file
- Checked for missing values
- Split the dataset into training and testing sets

## Machine Learning Model - Linear Regression (More Info):
Linear regression is suitable for predicting numerical outcomes with a linear relationship between features. We utilized multiple linear regression to capture the linear association between crime rate and multiple independent variables.

## Machine Learning Model - Random Forest (More Info):
Random forest, a supervised learning algorithm, leverages ensemble methods to solve regression and classification tasks. We employed random forest regression to aggregate predictions from multiple decision trees.

## Machine Learning Model - Neural Network (More Info):
In addition to linear regression and random forest, we experimented with neural network models, known for their ability to discern intricate patterns. Unlike linear regression, neural networks incorporate hidden layers to enhance prediction accuracy.

