x <- airquality
#Extract the first 2 rows of the data frame and print them to the console.
x[1:2, ]
#How many observations (i.e. rows, columns) are in this data frame?
nrow(x)
ncol(x)
#Extract the last 2 rows of the data frame and print them to the console.
tail(x, 2)
#What is the value of Ozone in the 47th row?
x[47, "Ozone"]
#How many missing values are in the Ozone column of this data frame?
sum(is.na(x$Ozone))
#What is the mean of the Ozone column in this dataset? Exclude missing values 
#(coded as NA) from this calculation.
mean(x$Ozone, na.rm = TRUE)
#Extract the subset of rows of the data frame where Ozone values are above 
#31 and Temp values are above 90. What is the mean of Solar.R in this subset?
subset <- x[x$Ozone > 31 & x$Temp > 90, ]
mean(subset$Solar, na.rm = TRUE)
#What is the mean of "Temp" when "Month" is equal to 6? 
subset <- x[x$Month == 6, ]
mean(subset$Temp, na.rm = TRUE)
#What was the maximum ozone value in the month of May (i.e. Month is equal to 5)?
subset <- x[x$Month == 5, ]
max(subset$Ozone, na.rm = TRUE)
