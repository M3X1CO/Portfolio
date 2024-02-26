library(readxl)
library(openxlsx)

heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 4)
heart_rate_data <- na.omit(heart_rate_data)

colnames(heart_rate_data) <- c("A", "B", "C")

runners_data <- heart_rate_data[heart_rate_data$B == "Control", ]
runners_values <- runners_data$C

standard_deviation <- sd(runners_values)
skewness <- skewness(runners_values)
kurtosis <- kurtosis(runners_values)

cat(sprintf("Standard Deviation: %.2f\n", standard_deviation))
cat(sprintf("Skewness: %.2f\n", skewness))
cat(sprintf("Kurtosis: %.2f\n", kurtosis))

library(stats)

# Shapiro-Wilk test
shapiro_test <- shapiro.test(runners_values)
cat("Shapiro-Wilk test result:\n")
print(shapiro_test)

library(goftest)
anderson_darling_test <- ad.test(runners_values)
cat("\nAnderson-Darling test result:\n")
print(anderson_darling_test)
