import matplotlib.pyplot as plt
import numpy as np

"""
You will now create a graph using streamflow data of the Provo River in June 2021.

Create and slice the array to create the x and y-axis values. These will correspond to the following columns in the CSV linked on the HW instructions page:
*   x = Date
*   y_1 = Site 10163000
*   y_2 = Site 10155200
*   y_3 = Site 10155500
*   y_4 = Site 10154200
*   y_5 = Site 10155000
"""

# Get data
provo_data = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',', dtype=str, skip_header=1)

x_provo = provo_data[:, 0]                          # Date (keep as string)
y_site_10163000 = provo_data[:, 1].astype(float)    # Convert streamflow values to numbers
y_site_10155200 = provo_data[:, 2].astype(float)
y_site_10155500 = provo_data[:, 3].astype(float)
y_site_10154200 = provo_data[:, 4].astype(float)
y_site_10155000 = provo_data[:, 5].astype(float)

"""
Plot x, y_1, y_2, y_3, y_4, and y_5 with the elements shown in the instructions in the code block below.
"""

# Graph the data
plt.figure(figsize=(10, 4))
plt.plot(x_provo, y_site_10163000, color='red', label='Site 10163000')
plt.plot(x_provo, y_site_10155200, color='blue', label='Site 10155200')
plt.plot(x_provo, y_site_10155500, color='green', label='Site 10155500')
plt.plot(x_provo, y_site_10154200, color='orange', label='Site 10154200')
plt.plot(x_provo, y_site_10155000, color='purple', label='Site 10155000')

plt.title('Provo River Streamflow Data')
plt.xlabel('Date')
plt.ylabel('Streamflow Rate')
plt.xticks(rotation=45)  # Optional: rotates dates so they don't overlap
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
