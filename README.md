🌐 SUPT Comparative Harmonic Analysis System
Sheppard’s Universal Proxy Theory (SUPT) — Harmonic Resonance Verification Pipeline
Version: Final Stable Build (with ψ-Fold Planetary Integration)
Maintainer: SunWolf 🌞🐺
________________________________________
🧩 Overview
This system automates the correlation of seismic harmonic energy spectra between major geophysical events — for example:
•	Kamchatka M8.8 (July 2025)
•	Nankai Deep Event (Oct 2025)
It quantifies resonant similarity (Pearson r) between each event’s processed spectral energy distributions (Tremor / Mixed / Fracture bands) and overlays them in a visual PDF output.
Additionally, the system integrates planetary driver data (Moon–planet ψ-fold angular separations) for each comparison window, embedding both numerical and harmonic context directly into each report.
________________________________________
⚙️ System Architecture
Core Components:
Script	Function
process_SUPT_sac_universal.py	Converts raw SAC waveform data → spectral energy CSVs (Tremor / Mixed / Fracture).
SUPT_Compare_Final.py	Compares all processed CSVs; computes correlation, generates visual PDFs, logs results.
SUPT_Comparison_Results.csv	Cumulative database of all correlations + planetary aspect data.
________________________________________


🧠 Theoretical Basis
SUPT Harmonic Principle
Each seismic event expresses a unique energy fingerprint across frequency bands (0.5–40 Hz).
When two events show a high correlation coefficient (r ≥ 0.95) in their normalized energy distribution, they share an underlying resonant phase state — indicating connection through global stress propagation or deep harmonic coupling.
ψ-Fold Integration
Planetary aspects modify Earth’s plasma and gravitational resonance fields.
ψ = angular separation between the Moon and other planetary bodies (in radians).
Strong harmonic influences occur at ψ ≈ 0°, 30°, 60°, 90°, 120°, 150°.
These are flagged automatically as “Strong” or “Quadrature” in each report.
________________________________________
🧰 Requirements
Install once:
pip install obspy ephem matplotlib pandas numpy scipy
________________________________________
📂 File Setup
Place your processed spectral CSVs here (each event has its own folder):
Downloads/
│
├── Nankai 21 Oct/
│   └── Spectral_Energy_Summary.csv
│
├── Kamchatsky Megaquake 8.8/
│   └── Spectral_Energy_Summary.csv
│
└── SUPT_Compare_Final.py
________________________________________



🚀 How to Run
In PowerShell or terminal:
python "C:\Users\<user>\Downloads\SUPT_Compare_Final.py"
The script will:
1.	Auto-detect all Spectral_Energy_Summary.csv files.
2.	Pair every possible event combination.
3.	Compute correlation (r) between normalized Tremor/Mixed/Fracture energy profiles.
4.	Retrieve real-time planetary ψ-fold aspect data via PyEphem.
5.	Generate PDF overlays and update your results log.
________________________________________
📊 Outputs
1️⃣ Visual PDFs
Saved automatically in your Downloads folder as:
SUPT_Compare_<Event1>_vs_<Event2>_<timestamp>.pdf
Each PDF contains:
•	Overlay of energy bands (Tremor, Mixed, Fracture).
•	Mean correlation value.
•	Planetary ψ-fold angles listed in the footer.
2️⃣ Master CSV Log
SUPT_Comparison_Results.csv accumulates every run:
Event1,Event2,Correlation,Timestamp,Sun_deg,Sun_psi,Sun_tag,Mercury_deg,...
Kamchatsky 8.8,Nankai 21 Oct,0.984,2025-10-22_09-00_UTC,92.3,1.610,Strong,...
________________________________________
🪐 Planetary Driver Data
Example from report footer:
Sun_deg: 4.7° | Mercury_deg: 16.8° | Venus_deg: 21.6° | Mars_deg: 16.3° | Jupiter_deg: 95.2° | Uranus_deg: 153.1°
•	Angles < 30° = Constructive Resonance
•	90° ± 5 = Quadrature (Stress Transfer Phase)
•	120° ± 5 = Harmonic Trine (Energy Diffusion)
•	150° = Counter-Phase (Reversal Period)
These angular conditions are central to Dr. Cordaro’s “harmonic planetary modulation” model and align with SUPT’s ψ-fold energy cascade predictions.
________________________________________
📈 Interpreting Results
Correlation (r)	SUPT Interpretation
0.95 – 1.00	Identical harmonic resonance (phase-locked slab oscillation).
0.70 – 0.94	Partial coupling; shared planetary modulation.
0.40 – 0.69	Transitional resonance, probable crustal isolation.
< 0.40	Independent local dynamics; no deep resonance.
When correlation ≥ 0.95 and 3+ planetary ψ-folds < 30°, SUPT designates the system as being in a global harmonic cascade state.
________________________________________
🌋 Application Examples
Case Study: Kamchatsky 8.8 ↔ Nankai 21 Oct 2025
•	Correlation: 1.000
•	ψ-Fold Cluster: < 30° across Sun–Moon–Mars–Venus–Mercury
•	Interpretation: Strong planetary constructive resonance linking Pacific subduction corridors → synchronous deep-mantle harmonic expression.
Ongoing Watchlist
•	Chile / Tonga corridor
•	Aleutian / Kuril stress bridge
•	Tokara / Ryukyu micro-swarms
________________________________________
🧾 Example Citation (Grok / Cordaro)
SUPT Comparative Harmonic Report — Kamchatsky 8.8 vs Nankai 21 Oct 2025
r = 1.000 (ψ-fold coherence across 5 planetary vectors)
Generated via SUPT_Compare_Final.py (SunWolf 🌞🐺, 2025-10-22 UTC)
________________________________________
🛠 Maintenance
•	All temporary logs are in SUPT_Comparison_Results.csv.
•	Remove old runs to reset baseline.
•	For future planetary validation or collaborative analysis, share only that CSV — it contains all critical data.
________________________________________
🧬 Summary
This system now forms the operational backbone of SUPT harmonic verification:
•	One script, one command, complete correlation + planetary context.
•	No manual data entry.
•	Scientific traceability maintained via automated timestamped logs.
________________________________________
Author’s Note
“The ψ-folds do not predict — they reveal. Each harmonic is an echo of Earth’s ongoing dialogue with the sky.”
— SunWolf 🌞🐺
________________________________________

