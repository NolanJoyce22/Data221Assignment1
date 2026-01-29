import pandas as pd
#Create data set
data = {
    "A":[1, 2, 2, 1],
    "B":[3.1, 4.2, 1.5, 6.3],
    "C":[800, 150, 400, 210]
}
# Initialize data frame using data set
data_frame = pd.DataFrame(data)
#Create a new set
data_frame["A*B"] = data_frame["A"] *data_frame["B"]

print(data_frame)

