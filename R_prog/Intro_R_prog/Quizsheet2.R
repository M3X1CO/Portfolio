#reading sheet 2 and seperating the variable gender into 2 excel documents for 
#male and female

library(readxl)
library(openxlsx)

heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 2)
heart_rate_data <- na.omit(heart_rate_data)

colnames(heart_rate_data) <- c("A", "B")

# Subset the data frame to only include male participants
male_participants <- heart_rate_data[heart_rate_data$A == "Male", ]

# Create a new data frame with only the male participants and their heart rates
df_male <- data.frame(C = male_participants$A, D = male_participants$B)

# Subset the original data frame to only include female participants
female_participants <- heart_rate_data[heart_rate_data$A != "Male",]

write.xlsx(df_male, "Male Participants.xlsx")
write.xlsx(female_participants, "Female Participants.xlsx")
