#reading sheet 2 and seperating the variable gender into 2 excel documents for 
#male and female

library(readxl)
library(openxlsx)

heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 4)
heart_rate_data <- na.omit(heart_rate_data)

colnames(heart_rate_data) <- c("A", "B", "C")

# Subset the data frame to only include male participants
fcontrol_participants <- heart_rate_data[heart_rate_data$A == "Female" & heart_rate_data$B == "Control", ]

# Subset the original data frame to only include female participants
mcontrol_participants <- heart_rate_data[heart_rate_data$A == "Male" & heart_rate_data$B == "Control", ]

write.xlsx(fcontrol_participants, "Female Control Participants.xlsx")
write.xlsx(mcontrol_participants, "Male Control Participants.xlsx")
