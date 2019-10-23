# DataCleaning-Basic-feature-engineering-techniques-to-the-regression-dataset.
Basic feature engineering techniques to the regression dataset. 

To-do list: 1. Import the necessary libraries. 
2. Import the dataset (final_dataset.csv) 
3. Remove columns with missing values greater than 40% of dataset size. 
4. Extract numeric data from columns property_price, square_area &amp; carpet_area using regular expressions. Make sure that units are standardized (all the values in property_price should be in lakhs)
5. In the above columns, fill empty values with mean of remaining data points 
6. Convert columns facing, overlooking, ownership, transaction, furnishing into categorical variables by assigning values [0,1,2…].  
7. In the above columns, fill empty values with 0.
8. Convert all values in the floor column to decimals. For example, convert “10 out of 14 floors” as 10/14 = 0.71.  
9. Fill empty values in floor and balcony with 0. 
