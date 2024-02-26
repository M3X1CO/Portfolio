x <- Sys.time()
p <- as.POSIXlt(x)
names(unclass(p))
p$sec
unclass(x)

datestring <- c("January 10, 2012 10:40", "December 9, 2011 9:10")
x <- strptime(datestring, "%B %d, %Y %H:%M")
x
class(x)