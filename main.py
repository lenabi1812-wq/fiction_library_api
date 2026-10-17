from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "title": "Дюна",
        "author": "Фрэнк Герберт",
        "genre": "Научная фантастика"
    },
    {
        "title": "Марсианин",
        "author": "Энди Вейер",
        "genre": "Научная фантастика"
    },
    {
        "title": "451° по Фаренгейту",
        "author": "Рэй Брэдбери",
        "genre": "Антиутопия"
    }
]

@app.get("/")
def read_root():
    return {
        "name": "API библиотеки фантастики",
        "path": "/books"
    }

@app.get("/books")
def read_books():
    return books