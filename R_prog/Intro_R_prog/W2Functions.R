add2 <- function(x, y) {
  x+y
}
above10 <- function(x) {
  use <- x > 10
  x[use]
}
columnmean <- function(y, removeNA = TRUE) {
  nc <- ncol(y)
  means <- numeric(nc)
  for(i in 1:nc) {
    means[i] <- mean(y[, i], na.rm = removeNA)
  }
  means
}
#columnmean(airquality) or columnmean(airquality, FALSE) provides the 
#call to a file and gets the mean data from each column

#r functions arguements can be matched positionally or by name. So the 
#following code calls to sd are all equivalent
mydata <- rnorm(100)
sd(mydata)
sd(x = mydata)
sd(x = mydata, na.rm = FALSE)
sd(na.rm = FALSE, x = mydata)
sd(na.rm = FALSE, mydata)
#So positional matching and matching by name can be mixed and this is
#quite useful often for functions that have very long argument lists.
args(lm)
function(formula, data, subset, weights, na.action,
          method = "qr", model = TRUE, singular.ok = TRUE,
          contrasts = NULL, offset, ...)
#lm(data = mydata, y - x, model = FALSE, 1:100)
#lm(y - x, mydata, 1:100, model = FALSE)

#defining a function
f <- function(a, b = 1, c = 2, d = NULL) {
}

#lazy evaluation
f <- function(a, b) {
  a ^ 2
}
#f(2) to get 2^2

f <- function(a, b) {
  print(a)
  print(b)
}
#f(45) gives the arguement for a but not for b and returns and error

# the ... arguement indicates a variable number of arguements that 
# are usually passed on to other functions
myplot <- function(x, y, type = "1", ...) {
  plot(x, y, type = type, ...)
}
# the ... arguement is also necessary when the number of arguements 
# passed to the function cannot be known in advance
args(paste)
function(..., sep = " ", collapse = NULL)
args(cat)
function(..., file = "", sep = " ", fill = FALSE,
         labels = NULL, append = FALSE)
#one catch with ... is that any arguements that appear after the ...
# on the arguement list must be named explicitly and cannot be partially 
# matched

args(paste)
function(..., sep = " ", collapse = NULL)

paste("a", "b", sep = ":")

paste("a", "b", se = ":")
