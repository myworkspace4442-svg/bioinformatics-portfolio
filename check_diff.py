import pandas as pd
import os

def compare_datasets(raw_path: str, processed_path: str):
    """
    မူရင်း Raw Data နှင့် သန့်စင်ပြီးသား Cleaned Data တို့၏ 
    ကွာခြားချက်များကို နှိုင်းယှဉ်ပြသခြင်း
    """
    print("🔍 [Comparison]: Raw Data နှင့် Cleaned Data တို့၏ ကွာခြားချက်များကို စစ်ဆေးနေပါပြီ...\n")
    
    if not os.path.exists(raw_path) or not os.path.exists(processed_path):
        print("❌ Error: လိုအပ်သော ဖိုင်တစ်ဖိုင်ခု မရှိပါ။ ETL Script ကို အရင် Run ပေးပါ။")
        return

    # ဒေတာများကို ဖတ်ရှုခြင်း
    df_raw = pd.read_csv(raw_path)
    df_processed = pd.read_csv(processed_path)
    
    # ၁။ Row အရွယ်အစား ကွာခြားချက်
    raw_rows = len(df_raw)
    processed_rows = len(df_processed)
    dropped_rows = raw_rows - processed_rows
    
    print("📊 --- Row အရေအတွက် ကွာခြားချက် ---")
    print(f"• မူရင်း Raw Data (Row ပေါင်း): {raw_rows:,}")
    print(f"• သန့်စင်ပြီး Cleaned Data (Row ပေါင်း): {processed_rows:,}")
    print(f"• ဖယ်ရှားလိုက်သည့် (Dropped) အမှိုက်/မလိုလားအပ်သော Rows: {dropped_rows:,}\n")
    
    # ၂။ Column အသစ်များ ကွာခြားချက်
    raw_cols = set(df_raw.columns)
    processed_cols = set(df_processed.columns)
    new_cols = processed_cols - raw_cols
    
    print("📋 --- Column များ ကွာခြားချက် ---")
    print(f"• မူရင်း Column များ: {list(raw_cols)}")
    print(f"• အသစ်တိုးလာသည့် Column များ: {list(new_cols)}\n")
    
    # ၃။ Sequence Length ရဲ့ အချက်အလက်များ
    if 'sequence_length' in df_processed.columns:
        min_len = df_processed['sequence_length'].min()
        max_len = df_processed['sequence_length'].max()
        mean_len = df_processed['sequence_length'].mean()
        
        print("🧬 --- Sequence Length အချက်အလက် (Cleaned Data) ---")
        print(f"• အတိုဆုံး Sequence အရှည်: {min_len} bp")
        print(f"• အရှည်ဆုံး Sequence အရှည်: {max_len} bp")
        print(f"• ပျမ်းမျှ (Average) Sequence အရှည်: {mean_len:.2f} bp")

if __name__ == "__main__":
    RAW_FILE = "train.csv"
    PROCESSED_FILE = "processed_data/cleaned_genomic_data.csv"
    
    compare_datasets(RAW_FILE, PROCESSED_FILE)