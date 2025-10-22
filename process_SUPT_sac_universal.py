import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from obspy import read

# === CONFIG ===
data_folder = r"C:\Users\benja\Downloads\Kamchatsky Megaquake 8.8"  # <-- adjust if needed
output_folder = os.path.join(data_folder, "processed_outputs")
os.makedirs(output_folder, exist_ok=True)

# === FREQUENCY BANDS (Hz) ===
bands = {
    "Tremor_Energy": (0.5, 5),
    "Mixed_Energy": (5, 15),
    "Fracture_Energy": (15, 40)
}

summary = []

print(f"\n📂 Reading SAC files from: {data_folder}")

# Find all SACs (case-insensitive)
sac_files = glob.glob(os.path.join(data_folder, "*.SAC")) + glob.glob(os.path.join(data_folder, "*.sac"))
if not sac_files:
    raise FileNotFoundError(f"No SAC files found in {data_folder}")

for sac_path in sac_files:
    try:
        st = read(sac_path)
        tr = st[0]
        tr.detrend("demean")
        tr.taper(0.05)
        tr.filter("bandpass", freqmin=0.5, freqmax=40.0)

        npts = tr.stats.npts
        dt = tr.stats.delta
        freqs = np.fft.rfftfreq(npts, dt)
        fft_vals = np.abs(np.fft.rfft(tr.data))
        total_energy = np.sum(fft_vals)

        band_energies = {}
        for label, (fmin, fmax) in bands.items():
            idx = np.where((freqs >= fmin) & (freqs < fmax))[0]
            band_energy = np.sum(fft_vals[idx]) if len(idx) > 0 else 0
            band_energies[label] = band_energy / total_energy * 100 if total_energy > 0 else 0

        summary.append({"File": os.path.basename(sac_path), **band_energies})

        # Spectrum plot
        plt.figure(figsize=(10, 5))
        plt.plot(freqs, fft_vals, color="black", lw=0.8)
        for label, (fmin, fmax) in bands.items():
            plt.axvspan(fmin, fmax, alpha=0.2, label=label)
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.title(f"{os.path.basename(sac_path)} – Spectral Energy")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, os.path.basename(sac_path) + "_spectrum.png"), dpi=200)
        plt.close()

        print(f"✅ Processed: {os.path.basename(sac_path)}")

    except Exception as e:
        print(f"⚠️ Error processing {os.path.basename(sac_path)}: {e}")

# Save unified summary
if summary:
    df = pd.DataFrame(summary)
    csv_path = os.path.join(output_folder, "Spectral_Energy_Summary.csv")
    df.to_csv(csv_path, index=False)
    print(f"\n✅ Complete! Saved standardized file:\n{csv_path}")
else:
    print("❌ No valid SAC data processed.")
