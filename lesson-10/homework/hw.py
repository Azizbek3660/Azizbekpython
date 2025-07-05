Homework 1. ToDo List Application

Define Task Class:
Create a Task class with attributes such as task title, description, due date, and status.
Define ToDoList Class:
Create a ToDoList class that manages a list of tasks.
Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
Create Main Program:
Develop a simple CLI to interact with the ToDoList.
Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
Test the Application:
Create instances of tasks and test the functionality of your ToDoList.
class Task:
    def __init__(self,title,description,due date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed=False
    def mark_conplete(self):
        self.completed=False
    def __str__(self):
        stetus="ok" if self.completed else 'no '
        return  f"{self.title} - {self.description} (Topshirish: {self.due_date})
class ToDoList:
    def __init__(self):
        self.tasks = []  # Bo‘sh ro‘yxat

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"'{title}' bajarildi deb belgilandi.")
                return
        print("Topshiriq topilmadi.")

    def list_all_tasks(self):
        if not self.tasks:
            print("Topshiriqlar yo‘q.")
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        found = False
        for task in self.tasks:
            if not task.completed:
                print(task)
                found = True
        if not found:
            print("Barcha topshiriqlar bajarilgan.")
def main():
    todo = ToDoList()

    while True:
        print("\n📋 ToDo List Menyusi")
        print("1. Topshiriq qo‘shish")
        print("2. Topshiriqni bajarilgan deb belgilash")
        print("3. Barcha topshiriqlarni ko‘rish")
        print("4. Bajarilmagan topshiriqlarni ko‘rish")
        print("5. Chiqish")

        choice = input("Tanlov (1-5): ")

        if choice == "1":
            title = input("Sarlavha: ")
            desc = input("Tavsif: ")
            due = input("Topshirish muddati: ")
            task = Task(title, desc, due)
            todo.add_task(task)
            print("✅ Topshiriq qo‘shildi.")

        elif choice == "2":
            title = input("Qaysi sarlavhadagi topshiriq bajarildi? ")
            todo.mark_complete(title)

        elif choice == "3":
            print("\n📄 Barcha topshiriqlar:")
            todo.list_all_tasks()

        elif choice == "4":
            print("\n📄 Faqat bajarilmagan topshiriqlar:")
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("✅ Dastur yakunlandi.")
            break

        else:
            print("❗️Noto‘g‘ri tanlov!")
if __name__ == "__main__":
    main()

   
✅ Homework 2: Simple Blog System
1. Post klassi:
python
Копировать код
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}\n{self.content}"
2. Blog klassi:
python
Копировать код
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("Postlar yo‘q.")
        for post in self.posts:
            print(post)
            print("—" * 40)

    def list_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author == author:
                print(post)
                print("—" * 40)
                found = True
        if not found:
            print("Muallif bo‘yicha post topilmadi.")

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print("Post o‘chirildi.")
                return
        print("Post topilmadi.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print("Post tahrirlandi.")
                return
        print("Post topilmadi.")

    def latest_posts(self, n=3):
        for post in self.posts[-n:]:
            print(post)
            print("—" * 40)
3. Main CLI dastur:
python
Копировать код
def main():
    blog = Blog()
    while True:
        print("\n📝 Blog Menyusi")
        print("1. Post qo‘shish")
        print("2. Barcha postlarni ko‘rish")
        print("3. Muallif bo‘yicha postlar")
        print("4. Postni o‘chirish")
        print("5. Postni tahrirlash")
        print("6. Eng so‘nggi postlar")
        print("7. Chiqish")

        tanlov = input("Tanlang (1-7): ")

        if tanlov == "1":
            title = input("Sarlavha: ")
            content = input("Matn: ")
            author = input("Muallif: ")
            blog.add_post(Post(title, content, author))

        elif tanlov == "2":
            blog.list_posts()

        elif tanlov == "3":
            author = input("Muallif nomi: ")
            blog.list_by_author(author)

        elif tanlov == "4":
            title = input("O‘chirmoqchi bo‘lgan post sarlavhasi: ")
            blog.delete_post(title)

        elif tanlov == "5":
            title = input("Tahrir qilinadigan post sarlavhasi: ")
            content = input("Yangi matn: ")
            blog.edit_post(title, content)

        elif tanlov == "6":
            blog.latest_posts()

        elif tanlov == "7":
            print("Dastur yakunlandi.")
            break

        else:
            print("❗️Noto‘g‘ri tanlov!")
python
Копировать код
if __name__ == "__main__":
    main()
