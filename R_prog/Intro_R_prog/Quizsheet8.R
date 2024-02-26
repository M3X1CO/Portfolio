library(readxl)
library(openxlsx)

heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 4)
heart_rate_data <- na.omit(heart_rate_data)

colnames(heart_rate_data) <- c("A", "B", "C")

library(moments)

standard_deviation <- sd(heart_rate_data$C)
skewness <- skewness(heart_rate_data$C)
kurtosis <- kurtosis(heart_rate_data$C)

cat(sprintf("Standard Deviation: %.2f\n", standard_deviation))
cat(sprintf("Skewness: %.2f\n", skewness))
cat(sprintf("Kurtosis: %.2f\n", kurtosis))