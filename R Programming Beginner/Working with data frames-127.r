## 2. Calling functions ##

# Define the add function.
add <- function(a, b){
    return(a + b)
}

# Call the add function with the arguments 1 and 2.
print(add(1, 2))
d = add(5, 10)

## 3. Defining a function ##

# Enter your code here.
subtract <- function(a, b){
    return(a - b)
}
d = subtract(50,10)

## 4. Reading in the data ##

# Enter your code here.
ufos = read.csv('ufo_sightings.csv')

## 5. Exploring the data frame ##

# Print the first 5 rows in the data frame.
print(head(ufos, 5))
print(tail(ufos, 5))