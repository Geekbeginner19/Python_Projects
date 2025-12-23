#Learning how to use matplotlib for data visualization

import matplotlib.pyplot as plt
import pandas as pd
# y = [1, 2, 3, 4, 5]
# x = [2, 4, 6, 7, 8]

# plt.plot(x, y)
# plt.show()

#Reading CSV files
Student_gamer_dataset = pd.read_csv(r"C:\Users\Rarissime\Downloads\Data Visualization\CSV Files\data.csv")
print(Student_gamer_dataset)

