import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ၁။ train.csv ဖိုင်ကို ဖတ်ခြင်း (ဖိုင်ရှိရာ path ကို ထည့်ပေးပါ)
df = pd.read_csv("train.csv")

# ၂။ DNA Sequence တစ်ခုချင်းစီ၏ အရှည် (Length) ကို တွက်ချက်၍ Column အသစ်ထည့်ခြင်း
df['sequence_length'] = df['sequence'].astype(str).apply(len)

# ၃။ Data Visualization (Distribution Graph ဆွဲခြင်း)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.histplot(df['sequence_length'], bins=30, kde=True, color="#4C72B0")

plt.title("DNA Sequence Length Distribution in Training Dataset", fontsize=14, fontweight="bold")
plt.xlabel("Sequence Length (Base Pairs)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

plt.tight_layout()
# ထွက်လာမယ့် Graph ကို ပုံဖိုင်အဖြစ် သိမ်းဆည်းခြင်း
plt.savefig("dna_length_distribution.png", dpi=300)
plt.show()

print("✅ Data Analysis ပြီးဆုံးပါပြီ။ Graph ပုံကို အောင်မြင်စွာ ထုတ်ယူနိုင်ပါပြီ။")