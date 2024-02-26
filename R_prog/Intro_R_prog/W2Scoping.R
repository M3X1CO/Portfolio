# how does r know which value to assign to which symbol when i type
lm <- function(x) {x * x}
#lm

#lexical scoping
f <- function(x, y) {
  x ^ 2 + y / z
}

make.power <- function(n) {
  pow <- function(x) {
    x^n
  }
  pow
}

cube <- make.power(3)
square <- make.power(2)
# call using
#cube(3) or square(3)

#whats in a functions environment
ls(environment(cube))
get("n", environment(cube))

#lexical scoping vs dynamic scoping
y <- 10
f <- function(x) {
  y <- 2
  y ^ 2 + g(x)
}
g <- function(x) {
  x * y
}