import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from datetime import datetime
import ephem  # planetary data

# === CONFIG ===
BASE_DIR = os.path.expanduser("~/Downloads")
PATTERN = "**/Spectral_Energy_Summary.csv"
RESULTS_LOG = os.path.join(BASE_DIR, "SUPT_Comparison_Results.csv")

# === UTILITIES ===
def clean_numeric(df):
    for col in df.columns:
        df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "").str.strip(), errors="coerce")
    return df.fillna(0)

def load_event_df(path):
    df = pd.read_csv(path)
    df = clean_numeric(df)
    name = os.path.basename(os.path.dirname(path))
    return name, df

def safe_corr(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    n = min(len(a), len(b))
    if n < 3: return np.nan
    try: return pearsonr(a[:n], b[:n])[0]
    except: return np.nan

def planetary_aspects(date):
    """Return Moon–planet angles (deg) and ψ (radians)."""
    obs = ephem.Observer(); obs.date = date
    moon = ephem.Moon(obs)
    bodies = ["Sun","Mercury","Venus","Mars","Jupiter","Uranus"]
    aspects = {}
    for b in bodies:
        p = getattr(ephem,b)(obs)
        diff = abs((moon.ra - p.ra)*180/np.pi)
        diff = diff if diff<=180 else 360-diff
        aspects[f"{b}_deg"] = round(diff,1)
        aspects[f"{b}_psi"] = round(np.deg2rad(diff),3)
        aspects[f"{b}_tag"] = "Strong" if (diff<30 or abs(diff-90)<5 or abs(diff-120)<5) else "Weak"
    return aspects

# === MAIN ===
csvs = glob.glob(os.path.join(BASE_DIR, PATTERN), recursive=True)
if len(csvs)<2:
    print("❌ Need at least two event datasets."); exit()
print(f"Found {len(csvs)} event summaries.")

events=[]
for f in csvs:
    try:
        n,d=load_event_df(f)
        events.append((n,d))
    except Exception as e:
        print("Skip",f,e)

results=[]
now=datetime.utcnow()

for i in range(len(events)):
    for j in range(i+1,len(events)):
        e1,df1=events[i]; e2,df2=events[j]
        n=min(len(df1),len(df2))
        df1=df1.iloc[:n]; df2=df2.iloc[:n]
        df1n=df1.select_dtypes(include=[np.number]); df2n=df2.select_dtypes(include=[np.number])
        corr=safe_corr(df1n.mean(axis=1),df2n.mean(axis=1))
        ts=now.strftime("%Y-%m-%d_%H-%M_UTC")
        aspects=planetary_aspects(now)
        row={"Event1":e1,"Event2":e2,"Correlation":round(corr,3),"Timestamp":ts,**aspects}
        results.append(row)

        # --- Plot ---
        plt.figure(figsize=(10,6))
        cols=df1n.columns[:min(3,len(df1n.columns))]
        for c in cols: plt.plot(df1n[c],"--",label=f"{e1}-{c}")
        for c in cols: plt.plot(df2n[c],label=f"{e2}-{c}")
        plt.title(f"{e1} vs {e2}\nMean Correlation = {corr:.3f}")
        plt.xlabel("Sample Index"); plt.ylabel("Relative Energy (%)"); plt.legend()
        footer="\n".join([f"{k}: {v}" for k,v in aspects.items() if k.endswith('_deg')])
        plt.figtext(0.5,0.02,footer,ha="center",fontsize=8)
        plt.tight_layout(rect=[0,0.05,1,1])

        out=os.path.join(BASE_DIR,f"SUPT_Compare_{e1}_vs_{e2}_{ts}.pdf")
        plt.savefig(out); plt.close()
        print(f"✅ {e1} ↔ {e2}: r={corr:.3f}")

# --- Save results log ---
dfres=pd.DataFrame(results)
if os.path.exists(RESULTS_LOG):
    old=pd.read_csv(RESULTS_LOG)
    dfres=pd.concat([old,dfres]).drop_duplicates(subset=["Event1","Event2"],keep="last")
dfres.to_csv(RESULTS_LOG,index=False)

print(f"\n🪐 Results saved:\n{RESULTS_LOG}\nPDFs in {BASE_DIR}")
