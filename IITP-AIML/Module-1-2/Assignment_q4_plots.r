
# Set up the plotting area to display 4 plots together
par(mfrow = c(2, 2))

values <- c(10, 20, 30, 40)
values
categories <- c("A", "B", "C", "D")
# Bar Graph
barplot(values, names.arg = categories, col = "blue", main = "Bar Graph", xlab = "Categories", ylab = "Values")

# Pie Chart
pie(values, labels = categories, main = "Pie Chart", col = rainbow(length(values)))

# Line Plot
plot(values, type = "o", col = "red", main = "Line Plot", xlab = "Index", ylab = "Values")

# Box Plot
boxplot(values, main = "Box Plot", col = "green", ylab = "Values")

