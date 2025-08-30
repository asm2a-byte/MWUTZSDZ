import pandas as pd
import matplotlib.pyplot as plt
from mwutsdz import MWUTSDZ

# === Load your dataset ===
# Replace with the path to your CSV or other data file
file_path = "your_dataset.csv"
df = pd.read_csv(file_path)

# === Select the appropriate columns ===
# Adjust these column names according to your dataset
cycles = df["Cycle_Index"]                 # or "cycle"
capacities = df["Discharge_Capacity (Ah)"] # or "capacity"

# === Apply MWUT-SDZ ===
# User-defined parameters:
# - windowSize: sliding window length
# - pThreshold: significance threshold for p-values
# - minRegionLength: minimum length (in cycles) to retain a region
model = MWUTSDZ(windowSize=5, pThreshold=0.01, minRegionLength=50)
results = model.fit(cycles, capacities)

# === Show results ===
print("📉 Significant regions (SDZ):", results["regions"])

# === Plot results ===
plt.figure(figsize=(10, 5))
plt.plot(cycles, capacities, label="Capacity", color="blue")

for start, end in results["regions"]:
    plt.axvspan(start, end, color="yellow", alpha=0.3, label="SDZ")

plt.xlabel("Cycle index")
plt.ylabel("Capacity (Ah)")
plt.title("Statistically Validated Degradation Zones (MWUT-SDZ)")
plt.legend()
plt.grid(True)
plt.show()
