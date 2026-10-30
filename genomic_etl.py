import pandas as pd
import os

def extract_data(file_path: str) -> pd.DataFrame:
    """
    [EXTRACT] - Raw Genomic CSV ဖိုင်မှ ဒေတာများကို ဖတ်ရှုခြင်း
    """
    print(f"📥 [Extract]: '{file_path}' မှ ဒေတာများကို စတင်ဖတ်ရှုနေပါပြီ...")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Error: {file_path} ဖိုင် မရှိပါ။")
    
    df = pd.read_csv(file_path)
    print(f"✅ Extract ပြီးဆုံးသည်: Row ပေါင်း {len(df)} ခု ရရှိပါသည်။")
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    [TRANSFORM] - ဒေတာများကို သန့်စင်ခြင်း၊ လိုအပ်သော Feature အသစ်များ တွက်ချက်ခြင်း
    """
    print("🔄 [Transform]: ဒေတာများကို စတင်သန့်စင်နေပါပြီ...")
    
    # ၁။ မလိုအပ်သော Missing values များ ဖြုတ်ထုတ်ခြင်း
    df = df.dropna(subset=['sequence', 'label'])
    
    # ၂။ DNA Sequence တစ်ခုချင်းစီ၏ အရှည် (Length) ကို တွက်ချက်၍ Column အသစ်ထည့်ခြင်း
    df['sequence_length'] = df['sequence'].astype(str).apply(len)
    
    # ၃. အမှားအယွင်းရှိသော အတိုအထွာ Sequence များကို ဖယ်ရှားခြင်း
    df_cleaned = df[df['sequence_length'] > 10].copy()
    
    print(f"✅ Transform ပြီးဆုံးသည်: သန့်စင်ပြီးနောက် Row ပေါင်း {len(df_cleaned)} ခု ကျန်ရှိပါသည်။")
    return df_cleaned

def load_data(df: pd.DataFrame, output_dir: str, output_filename: str):
    """
    [LOAD] - သန့်စင်ပြီးသား ဒေတာများကို Production/Portfolio အတွက် သပ်ရပ်သော Folder သို့ သိမ်းဆည်းခြင်း
    """
    print(f"📤 [Load]: ဒေတာများကို သိမ်းဆည်းနေပါပြီ...")
    
    # Output Directory မရှိသေးရင် ဖန်တီးခြင်း
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)
    
    # CSV အဖြစ် သိမ်းဆည်းခြင်း
    df.to_csv(output_path, index=False)
    print(f"✅ Success: ETL Pipeline အောင်မြင်ပါပြီ။ ဖိုင်ကို '{output_path}' တွင် သိမ်းဆည်းပြီးပါပြီ။")

if __name__ == "__main__":
    # Pipeline စတင်မည့် နေရာ
    RAW_INPUT = "train.csv"          # ကိုယ့်ဆီမှာရှိတဲ့ Raw Data ဖိုင်နာမည်
    OUTPUT_FOLDER = "processed_data" # ထွက်လာမယ့် သန့်စင်ပြီးသား ဖိုင်တွဲ
    OUTPUT_FILE = "cleaned_genomic_data.csv"
    
    try:
        # ETL အဆင့်ဆင့် လုပ်ဆောင်ခြင်း
        raw_data = extract_data(RAW_INPUT)
        transformed_data = transform_data(raw_data)
        load_data(transformed_data, OUTPUT_FOLDER, OUTPUT_FILE)
        
    except Exception as e:
        print(f"❌ ETL Pipeline Error: {str(e)}")