import pandas as pd

# مسیر فایل اکسل
file_path = "آهن سازی.xlsx"  # مسیر فایل اکسل خود را وارد کنید
sheet_name = "احیا مستقیم یک"

# تابع برای تبدیل داده‌ها به فرمت Aiken
# تابع برای تبدیل داده‌ها به فرمت Aiken
def convert_to_aiken_format(data):
    aiken_data = []
    for _, row in data.iterrows():
        question = row["متن سوال"]
        options = [
            f"A. {str(row['گزینه 1']).strip()}",
            f"B. {str(row['گزینه 2']).strip()}",
            f"C. {str(row['گزینه 3']).strip()}",
            f"D. {str(row['گزینه 4']).strip()}",
        ]
        correct_option = int(row["شماره گزینه صحیح"])  # شماره گزینه صحیح
        answer = ["A", "B", "C", "D"][correct_option - 1]  # تبدیل شماره به حرف

        # ساختار فرمت Aiken
        aiken_data.append(question)
        aiken_data.extend(options)
        aiken_data.append(f"ANSWER: {answer}")
        aiken_data.append("")  # خط خالی بین سوالات

    return "\n".join(aiken_data)


# خواندن داده‌ها از شیت
data = pd.read_excel(file_path, sheet_name=sheet_name)

# تبدیل داده‌ها به فرمت Aiken
aiken_output = convert_to_aiken_format(data)

# ذخیره در فایل خروجی
output_file = "output_ehya1.txt"  # نام فایل خروجی
with open(output_file, "w", encoding="utf-8") as file:
    file.write(aiken_output)

print(f"فایل به فرمت Aiken ذخیره شد: {output_file}")
