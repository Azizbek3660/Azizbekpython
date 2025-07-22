[
  {
    "name": "Ali",
    "age": 21,
    "major": "Computer Science"
  },
  {
    "name": "Laylo",
    "age": 22,
    "major": "Mathematics"
  }
]

import json
with open("students.json", "r") as f:
    students = json.load(f)

# Har bir talaba haqida ma'lumot chiqarish
for student in students:
    print("Ism:", student.get("name"))
    print("Yosh:", student.get("age"))
    print("Mutaxassislik:", student.get("major"))
    print("-" * 30)
Task: Weather API
Use this url : https://openweathermap.org/
Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests
api_key="8d4dcd2097e06acd0bf8b48fdaf577e0"
city="Tashkent"
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
data=response.json()
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]
city_name = data["name"]
print(f"Shahar: {city_name}")
print(f"Temperatura: {temperature}°C")
print(f"Namlik: {humidity}%")
print(f"Ob-havo: {description}")
print(f"Shamol tezligi: {wind_speed} m/s")

Task: JSON Modification
Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
[
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "year": 2018
  },
  {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988
  }
]

import json

# JSON faylni o‘qish
def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# JSON faylga yozish
def save_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)


def add_book():
    books = load_books()
    
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = int(input("Yili: "))
    
    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    
    books.append(new_book)
    save_books(books)
    print(f"✅ '{title}' kitobi qo‘shildi.")
#✅ 4-QADAM: Kitobni yangilash funksiyasi
#python
#Копировать код
def update_book():
    books = load_books()
    title = input("Qaysi kitobni yangilamoqchisiz? Nomi: ")
    
    for book in books:
        if book["title"].lower() == title.lower():
            book["author"] = input("Yangi muallif: ")
            book["year"] = int(input("Yangi yil: "))
            save_books(books)
            print(f"✏️ '{title}' yangilandi.")
            return
    
    print("⚠️ Kitob topilmadi.")

def delete_book():
    books = load_books()
    title = input("Qaysi kitobni o‘chirmoqchisiz? Nomi: ")
    
    updated_books = [book for book in books if book["title"].lower() != title.lower()]
    
    if len(books) == len(updated_books):
        print("⚠️ Kitob topilmadi.")
    else:
        save_books(updated_books)
        print(f"🗑️ '{title}' kitobi o‘chirildi.")

def main():
    while True:
        print("\n📚 KITOBLAR BAZASI")
        print("1. Kitob qo‘shish")
        print("2. Kitobni yangilash")
        print("3. Kitobni o‘chirish")
        print("4. Chiqish")
        
        choice = input("Tanlov (1-4): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("👋 Dasturdan chiqildi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov. Qaytadan urinib ko‘ring.")

main()

Task: Movie Recommendation System
Use this url http://www.omdbapi.com/ to fetch information about movies.
Create a program that asks users for a movie genre and recommends a random movie from that genre.
api_key="dd1f8e95"
import requests
import random
api_key="dd1f8e95"
search_terms=["life", "war", "love", "dark", "day", "night", "hero", "man", "dream", "game"]
def get_movies_by_genre(genre):
    movies = []

    for term in search_terms:
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={term}&type=movie"
        response = requests.get(url)
        data = response.json()

        if data.get("Search"):
            for item in data["Search"]:
                imdb_id = item["imdbID"]
                # Film haqida to‘liq ma’lumot olish
                detail_url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}"
                detail_response = requests.get(detail_url)
                detail_data = detail_response.json()

                if genre.lower() in detail_data.get("Genre", "").lower():
                    movies.append(detail_data)

    return movies

def recommend_movie():
    genre = input("Qaysi janrdagi filmni xohlaysiz? (masalan: Action, Drama, Comedy): ")
    matched_movies = get_movies_by_genre(genre)

    if matched_movies:
        movie = random.choice(matched_movies)
        print("\n🎬 Siz uchun tavsiya:")
        print("Nomi:", movie["Title"])
        print("Yil:", movie["Year"])
        print("Janr:", movie["Genre"])
        print("Rejissor:", movie["Director"])
        print("IMDb reyting:", movie["imdbRating"])
        print("Qisqacha:", movie["Plot"])
    else:
        print("❌ Kechirasiz, bu janrga mos film topilmadi.")
