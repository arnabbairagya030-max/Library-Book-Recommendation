
import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL
)
""")

# Insert books
books = [
    ("Python Programming", "Reema Thareja", "Programming"),
    ("Let Us C", "Yashavant Kanetkar", "Programming"),
    ("Wings of Fire", "APJ Abdul Kalam", "Biography"),
    ("The Alchemist", "Paulo Coelho", "Fiction"),
    ("Rich Dad Poor Dad", "Robert Kiyosaki", "Finance"),
    ("Introduction to AI", "Stuart Russell", "Artificial Intelligence")
]

cursor.executemany("""
INSERT INTO books (title, author, category)
VALUES (?, ?, ?)
""", books)

# Save changes
conn.commit()

print("Database created successfully!")

# Close connection
conn.close()
