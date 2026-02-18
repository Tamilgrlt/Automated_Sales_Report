import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV file
data = pd.read_csv("sales_data.csv")

# Step 2: Calculate Total Price
data["Total Price"] = data["Quantity"] * data["Price"]

# Step 3: Create Bar Graph
plt.figure()
plt.bar(data["Product"], data["Total Price"])
plt.xlabel("Product")
plt.ylabel("Total Sales Amount")
plt.title("Product-wise Sales Graph")
plt.xticks(rotation=30)
plt.tight_layout()

# Step 4: Save Graph
plt.savefig("sales_graph.png")
plt.close()

print("Graph created successfully")
