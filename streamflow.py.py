import numpy as np
import matplotlib.pyplot as plt


def load_streamflow(filename):
  """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
  provo_data = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
  dates = provo_data[:, 0]
  flows = provo_data[:, 1:6].astype(float)
  return dates, flows


def plot_streamflow(dates, flows, sites):
  """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
  colors = ['red', 'blue', 'green', 'orange', 'purple']

  plt.figure(figsize=(10, 4))
  for i in range(len(sites)):
   plt.plot(dates, flows[:, i], color=colors[i], label=f'Site {sites[i]}')

  plt.title('Provo River Streamflow Data')
  plt.xlabel('Date')
  plt.ylabel('Streamflow Rate')
  plt.xticks(rotation=45)
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
