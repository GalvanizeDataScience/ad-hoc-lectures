iris$Nonsense <- rnorm(nrow(iris))
print(iris)
write.csv(iris, file = 'iris.csv')

# on another computer
iris <- read.csv('iris.csv')
