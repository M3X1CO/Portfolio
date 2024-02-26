#read the first sheet, print all the data from the word variable to source the
#headers in the xlsx file
library(readxl)
heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 1)
heart_rate_data <- na.omit(heart_rate_data)
variable_row <- which(heart_rate_data[,1] == "Variables")
source_row <- which(heart_rate_data[,1] == "Source")
print(heart_rate_data[(variable_row+1):(source_row-1),])

#rewrite to print only the variables
heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 1)
heart_rate_data <- na.omit(heart_rate_data)
variable_row <- which(heart_rate_data[,1] == "Variables")
source_row <- which(heart_rate_data[,1] == "Source")
section_of_interest <- heart_rate_data[(variable_row+1):(source_row-1),]
lines_to_print <- c(1, 4, 9)
print(section_of_interest[lines_to_print, ])

#print to file
library(readxl)
heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 1)
heart_rate_data <- na.omit(heart_rate_data)
variable_row <- which(heart_rate_data[,1] == "Variables")
source_row <- which(heart_rate_data[,1] == "Source")
section_of_interest <- heart_rate_data[(variable_row+1):(source_row-1),]
lines_to_write <- c(1, 4, 9)
selected_lines <- section_of_interest[lines_to_write, ]
writeLines(as.character(selected_lines[,1]), con = "Variables.txt")

#make a list with data
library(readxl)
heart_rate_data <- read_excel("Dataset_Heart Rate.xlsx", sheet = 1)
heart_rate_data <- na.omit(heart_rate_data)
variable_row <- which(heart_rate_data[,1] == "Variables")
source_row <- which(heart_rate_data[,1] == "Source")
section_of_interest <- heart_rate_data[(variable_row+1):(source_row-1),]
lines_to_write <- c(1, 4, 9)
selected_lines <- section_of_interest[lines_to_write, ]
list_of_lines <- as.list(selected_lines[,1])