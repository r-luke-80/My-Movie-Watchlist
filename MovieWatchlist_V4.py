import tkinter as tk

# Creates a list and stores movies in memory 
movies = []


def add_movie():
    """Adds a movie (title + genre) to the in-memory watchlist."""
    title = title_entry.get().strip()
    genre = genre_entry.get().strip()

    # Basic validation
    if title == "" or genre == "":
        status_label.config(text="Please fill in both fields.")
        return

    # Store in memory (simple format for now)
    movie = f"{title}|{genre}"
    movies.append(movie)

    # Feedback to the user
    status_label.config(text="Movie added!")

    # Clear input boxes
    title_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)


# MAIN WINDOW
root = tk.Tk()
root.title("Movie Watchlist Manager - Project Status 2")

# Movie Title input
tk.Label(root, text="Movie Title").pack()
title_entry = tk.Entry(root)
title_entry.pack()

# Genre input
tk.Label(root, text="Genre").pack()
genre_entry = tk.Entry(root)
genre_entry.pack()

# Button
tk.Button(root, text="Add Movie", command=add_movie).pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()