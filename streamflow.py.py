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
  plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
  plt.show()

def summarize(dates, flows, sites):
  """Print summary statistics for each gauge."""
  header = f"{'Gauge' :<10}{'Max (cfs)':>10} {'Date of max':<18} {'Min (cfs)':>10} {'Avg (cfs)':>10}"
  print(header)

  with open('streamflow_summary.csv', 'w') as f:
    f.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")
    
    for i in range(len(sites)):
      col = flows[:, i]
      max_flow = np.max(col)
      max_idx = np.argmax(col)
      date_of_max = dates[max_idx]
      min_flow = np.min(col)
      avg_flow = np.mean(col)

      print(f"{sites[i]:<10}{max_flow:>10.2f} {date_of_max:<18} {min_flow:>10.2f} {avg_flow:>10.2f}")
      f.write(f"{sites[i]},{max_flow:.2f},{date_of_max},{min_flow:.2f},{avg_flow:.2f}\n")

# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summarize(dates, flows, sites)

# Prompt the user for a streamflow threshold in cfs and convert the input string to a float
threshold = float(input("\nEnter a flow threshold (cfs): "))

# Loop through each gauge and calculate how many hours the flow exceeded the threshold
print(f"\nHours above {threshold} cfs in June 2021:")
for i in range(len(sites)):
    # Create a boolean array where True indicates readings above the threshold, then sum them
    readings_above = np.sum(flows[:, i] > threshold)
    # Multiply the count of 15-minute readings by 0.25 to convert to hours
    hours_above = readings_above * 0.25
    print(f"Gauge {sites[i]}: {hours_above:.2f} hours")


plot_streamflow(dates, flows, sites)
