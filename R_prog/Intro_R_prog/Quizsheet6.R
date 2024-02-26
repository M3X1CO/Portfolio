library(dplyr)

heart_rate_data <- read_excel("Female Control Participants.xlsx",)
colnames(heart_rate_data) <- c("A", "B", "C")
heart_rate_data <- na.omit(heart_rate_data)
heart_rate_data$C <- as.numeric(heart_rate_data$C)

# Remove any non-integer rows from the heart rate data
heart_rate_data <- filter(heart_rate_data, C %% 1 == 0)

# Calculate the average of the heart rate column
average_heart_rate <- mean(heart_rate_data$C)

# Calculate the median of the heart rate column
median_heart_rate <- median(heart_rate_data$C)

# Display both the average and median with 2 decimal places
cat(sprintf("Average Heart Rate: %.2f\n", average_heart_rate))
cat(sprintf("Median Heart Rate: %.2f\n", median_heart_rate))
