#creating an object x with value 0:10
x <- 0:10
#calling objects class
class(x)
#changing output to numeric
as.numeric(x)
#asking if logical, true/false
as.logical(x)
#changing output to characters
as.character(x)
#creating a list and calling it
x <- list(1, "a", TRUE, 1 + 4i)
x
#creating a matrix, calling it, asking dim and attributes
m <- matrix(nrow = 2, ncol = 3)
m
dim(m)
attributes(m)
#matrix of 1 through 6 in 2 row 3 column
m <- matrix(1:6, nrow = 2, ncol = 3)
m
#simplified matrix 
m <- 1:10
m
dim(m) <- c(2,5)
m
x <- 1:3
y <- 10:12
cbind(x,y)
rbind(x,y)
#factors
x <- factor(c("yes", "yes", "no", "yes", "no"),
#create a baseline level system usually alphabetical order
levels = c("yes", "no"))
x
table(x)
unclass(x)
#data frames
x <- data.frame(foo = 1:4, bar = c(T, T, F, F))
x
nrow(x)
ncol(x)
#creating an object name for easier identification in writing
x <- 1:3
names(x)
names(x) <- c("foo", "bar", "norf")
x
names(x)
#creating a list with named objects
x <- list(a = 1, b = 2, c = 3)
x
#naming matrixices
m <- matrix(1:4, nrow = 2, ncol = 2)
dimnames(m) <- list(c("c", "d"), c("a", "b"))
m
#principle functions of reading data into R
#read.table, read.scv
#readLines
#source, which is inverse of dump
#dget read r code, inverse of dput
#load read saved workspaces
#unserialize for reading object in binary form from file
#analogous functions for writing data to files
#write.table
#writeLines
#dump
#dput
#save
#serialize
#how to move value of x to binary and store in a file then read binary to output R code
con <- file("myfile.bin", "wb")
serialize(x, connection = con)
close(con)
con <- file("myfile.bin", "rb")
unserialize(con)
close(con)
#subsetting lists
#how to extract multiple elements from a list can only use single bracket operator
x <- list(foo = 1:4, bar = 0.6, baz = "hello")
x[c(1, 3)]
#[[]] can take an integer sequence
x <- list(a = list(10, 12, 14), b = c(3.14, 2.81))
x[[c(1, 3)]]
x[[1]][[3]]
x[[c(2, 1)]]
#matrices can be subsetted in the usual way with (i, j) type indices
x <- matrix(1:6, 2, 3)
x[1, 2]
x[2, 1]
#matrices can also be missing
x[1, ]
x[, 2]
#by default, when a single element of a matrix is retrieved, it is returned as a vector of length 1 rather
#than a 1 x 1 matrix. This can be turned of by setting drop = FALSE
x <- matrix(1:6, 2, 3)
x[1, 2]
x[1, 2, drop = FALSE]
x[1, ]
x[1, , drop = FALSE]
#partial matching of names is allowed in [[]] and $
x <- list(aardvark = 1:5)
x$a
x[["a"]]
x[["aar", exact = FALSE]]
#removing missing values, na
x <- c(1, 2, NA, 4, NA, 5)
bad <- is.na(x)
x[!bad]
#what if there are multiple things and you want to take the subset with no missing values
x <- c(1, 2, NA,4, NA, 5)
y <- c("a", "b", NA, "d", NA, "f")
good <- complete.cases(x, y)
good
x[good]
y[good]
#removing NA values larger sets
airquality[1:6, ]
good <- complete.cases(airquality)
airquality[good, ][1:6, ]
#vectorized operations in R are vectorized making code more efficient, concise , and easier to read
x <- 1:4; y <- 6:9
x + y
x > 2
x >= 2
y == 8
x * y
x / y
# add subtract multiple and divide matrix
x <- matrix(1:4, 2, 2); y <- matrix(rep(10, 4), 2, 2)
x * y
x / y
x %*% y #true matrix multiplication!!!
#quiz
x <- 4
class(x)
x <- c(4, "a", TRUE)
class(x)
x <- c(1, 3, 5)
y <- c(3, 2, 10)
cbind(x, y)

