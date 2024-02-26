library(readxl)
library(openxlsx)

heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 4)
heart_rate_data <- na.omit(heart_rate_data)

colnames(heart_rate_data) <- c("A", "B", "C")

# Subset the data frame to only include female participants in the control group
fcontrol_participants <- heart_rate_data[heart_rate_data$A == "Female" & heart_rate_data$B == "Control", c("A", "B", "C")]

# Subset the data frame to only include male participants in the control group
mcontrol_participants <- heart_rate_data[heart_rate_data$A == "Male" & heart_rate_data$B == "Control", c("A", "B", "C")]

# Create a new workbook
wb <- createWorkbook()

# Add a sheet to the workbook
addWorksheet(wb, "Control Participants")

# Combine the data from female and male participants into a single data frame
combined_data <- rbind(fcontrol_participants, mcontrol_participants)

# Write the combined data to the sheet
writeData(wb, "Control Participants", combined_data)

# Save the workbook
file.remove("Combined Control Participants.xlsx")
saveWorkbook(wb, "Combined Control Participants.xlsx")
