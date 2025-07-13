Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
import datetime
date_of_birthdate=input('enter you birth date (YYYY-MM-DD formatda):')
date_of_birth = datetime.datetime.strptime(date_of_birthdate, "%Y-%m-%d").date()
today=datetime.date.today()
age=today-date_of_birth 
total_days = age.days
years = total_days // 365
months = (total_days % 365) // 30
days = (total_days % 365) % 30
print(f"Sizning yoshingiz: {years} yil, {months} oy, {days} kun.")



Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
import datetime
date_of_birthdate=input('enter you birth date (YYYY-MM-DD formatda):')
date_of_birth = datetime.datetime.strptime(date_of_birthdate, "%Y-%m-%d").date()
today=datetime.date.today()
current_year_birthday = date_of_birth.replace(year=today.year)
if current_year_birthday < today:
   
    next_birthday = date_of_birth.replace(year=today.year + 1)
else:
    next_birthday = current_year_birthday


days_left = (next_birthday - today).days

print(f"Keyingi tug‘ilgan kuningizgacha {days_left} kun qoldi.")
Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
from datetime import datetime, timedelta

# Foydalanuvchidan hozirgi sana va vaqtni olish
current_dt_str = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
current_dt = datetime.strptime(current_dt_str, '%Y-%m-%d %H:%M')

# Davomiylikni soat va daqiqalarda olish
hours = int(input("Uchrashuv davomiyligi (soat): "))
minutes = int(input("Uchrashuv davomiyligi (daqiqalar): "))

# Tugash vaqtini hisoblash
meeting_duration = timedelta(hours=hours, minutes=minutes)
end_time = current_dt + meeting_duration

# Natijani chiqarish
print("Uchrashuv tugash vaqti:", end_time.strftime("%Y-%m-%d %H:%M"))
Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz
# Foydalanuvchidan kirish
input_dt_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
from_timezone_str = input("Hozirgi vaqt zonangiz (masalan: Asia/Tashkent): ")
to_timezone_str = input("Qaysi vaqt zonasiga o‘girishni xohlaysiz? (masalan: Europe/London): ")

try:
    # Stringdan datetime yaratish
    naive_dt = datetime.strptime(input_dt_str, "%Y-%m-%d %H:%M")

    # Vaqt zonalarini olish
    from_timezone = pytz.timezone(from_timezone_str)
    to_timezone = pytz.timezone(to_timezone_str)

    # Datetime obyektiga vaqt zonasini biriktirish
    localized_dt = from_timezone.localize(naive_dt)

    # Aylantirish
    converted_dt = localized_dt.astimezone(to_timezone)

    # Natijani chiqarish
    print("Aylantirilgan vaqt:", converted_dt.strftime("%Y-%m-%d %H:%M (%Z)"))

except Exception as e:
    print("Xatolik yuz berdi:", e)
    print("Iltimos, vaqt va timezone nomlarini to‘g‘ri kiriting.")
import time
from datetime import datetime

# Foydalanuvchidan kelajakdagi sana-vaqtni olish
future_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")

# Stringni datetime obyektiga aylantirish
future_dt = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

print("\n⏳ Countdown boshlandi...\n")

# Doimiy tekshirish
while True:
    now = datetime.now()
    remaining = future_dt - now

    if remaining.total_seconds() <= 0:
        print("⏰ Vaqt tugadi!")
        break

    # Qolgan vaqtni formatlash
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Ekranga chiqarish
    print(f"Qolgan vaqt: {days} kun, {hours:02} soat, {minutes:02} daqiqa, {seconds:02} soniya", end="\r")

    time.sleep(1)  # 1 son
Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re

# Emailni so‘rash
email = input("Email manzilini kiriting: ")

# Email formatini tekshiruvchi regex
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Tekshirish
if re.match(pattern, email):
    print("✅ Email manzili to‘g‘ri formatda.")
else:
    print("❌ Email manzili noto‘g‘ri formatda!")
Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
import re

# Foydalanuvchidan raqamni olish
raw_number = input("Telefon raqamingizni kiriting (faqat raqamlar, masalan: 1234567890): ")

# Faqat raqamlarni olish (agar foydalanuvchi + yoki - kiritsa, ularni olib tashlaydi)
digits = re.sub(r'\D', '', raw_number)

# Formatlash
if len(digits) == 10:
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    print("Formatlangan raqam:", formatted)
else:
    print("❌ Raqam noto‘g‘ri. Iltimos, 10 xonali raqam kiriting.")
import re

password = input("Parolingizni kiriting: ")

# Shartlar
length_ok = len(password) >= 8
has_upper = re.search(r"[A-Z]", password)
has_lower = re.search(r"[a-z]", password)
has_digit = re.search(r"\d", password)

if length_ok and has_upper and has_lower and has_digit:
    print("✅ Parol mustahkam.")
else:
    print("❌ Parol zaif. Quyidagilarga amal qiling:")
    if not length_ok:
        print("- Kamida 8 ta belgidan iborat bo‘lishi kerak")
    if not has_upper:
        print("- Kamida bitta katta harf bo‘lishi kerak")
    if not has_lower:
        print("- Kamida bitta kichik harf bo‘lishi kerak")
    if not has_digit:
        print("- Kamida bitta raqam bo‘lishi kerak")
2️⃣ Word Finder (matndan so‘z qidirish)
python
Копировать код
import re

text = """
Python is a powerful programming language. Many developers love Python because of its simplicity.
Python can be used for web development, data science, automation, and more.
"""

word = input("Qidiriladigan so‘zni kiriting: ")
matches = re.findall(fr'\b{word}\b', text, re.IGNORECASE)

if matches:
    print(f"✅ So‘z '{word}' {len(matches)} marta topildi.")
else:
    print(f"❌ So‘z '{word}' matnda topilmadi.")
3️⃣ Date Extractor (matndan sana ajratish)
python
Копировать код
import re

text = input("Matn kiriting (matnda sanalar bo‘lishi mumkin): ")

# Sana formatlari: 2025-07-13 yoki 13/07/2025 va h.k.
date_pattern = r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b'

dates = re.findall(date_pattern, text)

if dates:
    print("✅ Matndan topilgan sanalar:")
    for d in dates:
        print("-", d)
else:
    print("❌ Matnda sana topilmadi.")
