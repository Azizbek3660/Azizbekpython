import sqlite3
import pandas as pd
conn = sqlite3.connect("chinook.db")
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId, Total FROM Invoice", conn)
customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM Custome
customer_totals = invoices.groupby("CustomerId")["Total"].sum().reset_index()
customer_totals.rename(columns={"Total": "TotalSpent"}, inplace=True
merged = pd.merge(customer_totals, customers, on="CustomerId")
merged["CustomerName"] = merged["FirstName"] + " " + merged["LastName"]
top5 = merged.sort_values(by="TotalSpent", ascending=False).head(5)
natija = top5[["CustomerId", "CustomerName", "TotalSpent"]]
print(natija)
import sqlite3
import pandas as pd

# 1. Ma'lumotlar bazasiga ulanamiz
conn = sqlite3.connect("chinook.db")

# 2. Kerakli jadvallarni o‘qib olamiz
invoice_lines = pd.read_sql_query("SELECT InvoiceId, TrackId FROM InvoiceLine", conn)
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM Invoice", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)

# 3. InvoiceLine va Invoice jadvalini birlashtirib, har bir xaridga mijozni qo‘shamiz
sales = pd.merge(invoice_lines, invoices, on="InvoiceId")

# 4. Track jadvali bilan birlashtirib, har bir trek qaysi albomga tegishli ekanini aniqlaymiz
sales = pd.merge(sales, tracks, on="TrackId")

# 5. Endi har bir albomda nechta trek borligini hisoblaymiz
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracks"}, inplace=True)

# 6. Mijoz albomdan nechta trek sotib olganini hisoblaymiz
customer_album_tracks = sales.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index()
customer_album_tracks.rename(columns={"TrackId": "TracksPurchased"}, inplace=True)

# 7. To‘liq albommi yoki yo‘qligini tekshiramiz
customer_album_tracks = pd.merge(customer_album_tracks, album_track_counts, on="AlbumId")
customer_album_tracks["BoughtFullAlbum"] = customer_album_tracks["TracksPurchased"] == customer_album_tracks["TotalTracks"]

# 8. Har bir mijoz uchun tekshiramiz: agar u *hech qachon* to‘liq albom olmagan bo‘lsa → "individual track" xaridori
customer_pref = customer_album_tracks.groupby("CustomerId")["BoughtFullAlbum"].any().reset_index()
customer_pref["Preference"] = customer_pref["BoughtFullAlbum"].apply(lambda x: "Full Album" if x else "Individual Tracks")

# 9. Har bir kategoriya bo‘yicha foizni hisoblaymiz
summary = customer_pref["Preference"].value_counts(normalize=True) * 100
summary = summary.reset_index()
summary.columns = ["Preference", "Percentage"]

# 10. Natijani chiqaramiz
print(summary)
