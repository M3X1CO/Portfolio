
#Nested for loop with matrix
x <- matrix(1:20, 4, 5)
for(i in seq_len(nrow(x)))   {
  for(j in seq_len(ncol(x)))   {
    print(x[i, j])
  }
}
x
#Just a while
count <- 0
while(count < 10)   {
  print(count)
  count <- count + 1
}
count
#more then 1 condition while loop, nested if/else
z <- 5
while(z >= 3 && z <= 10)    {
  print(z)
  coin <- rbinom(1, 1, 0.5)
  
  if(coin == 1)    { ## random walk
    z <- z + 1
  } else {
      z <- z - 1
    }
}
z
#repeat stuffs broken computeFunction is not a real function
x0 <- 1
tol <- 1e-8
repeat {
  x1 <- computeEstimate()
  
  if(abs(x1 - x0) < tol) {
    break
  } else {
    x0 <- x1
  }
}
x0
x1