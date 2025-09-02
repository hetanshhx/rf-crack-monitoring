#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# Hardcoded paths
txt_in = "data/s_para/dual_antenna_s11.txt"
out_png = "figures/s11_vs_freq.png"

# Load TXT (CST format, space-delimited, ignore # lines)
df = pd.read_csv(txt_in, delim_whitespace=True, comment='#', header=None)
df.columns = ["freq_GHz", "S11_dB"]

# Plot
plt.figure(figsize=(6,4))
plt.plot(df['freq_GHz'], df['S11_dB'], marker='o')
plt.xlabel('Frequency (GHz)')
plt.ylabel('S11 (dB)')
plt.title('S11 vs Frequency')
plt.grid(True)
plt.tight_layout()

# Save
plt.savefig(out_png, dpi=300)
print(f"Plot saved to {out_png}")
