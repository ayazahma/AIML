par(mfrow = c(3, 2))

# Generating Poisson Distribution
poisson_dist <- rpois(n = 20, lambda = 5)
cat("Poisson Distribution:\n", poisson_dist, "\n\n")
hist(poisson_dist, main = "Histogram of Poisson Distribution", xlab = "Values", col = "blue")

# Generating Normal Distribution
normal_dist <- rnorm(n = 20, mean = 0, sd = 1)
cat("Normal Distribution:\n", normal_dist, "\n\n")
hist(normal_dist, main = "Histogram of Normal Distribution", xlab = "Values", col = "green")

# Generating Geometric Distribution
geometric_dist <- rgeom(n = 20, prob = 0.5)
cat("Geometric Distribution:\n", geometric_dist, "\n\n")
hist(geometric_dist, main = "Histogram of Geometric Distribution", xlab = "Values", col = "red")

# Generating Binomial Distribution
binomial_dist <- rbinom(n = 20, size = 10, prob = 0.5)
cat("Binomial Distribution:\n", binomial_dist, "\n\n")
hist(binomial_dist, main = "Histogram of Binomial Distribution", xlab = "Values", col = "purple")

# Generating Uniform Distribution
uniform_dist <- runif(n = 20, min = 0, max = 1)
cat("Uniform Distribution:\n", uniform_dist, "\n\n")
hist(uniform_dist, main = "Histogram of Uniform Distribution", xlab = "Values", col = "orange")
