class Publication:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title

    def set_author(self, author):
        self._author = author

    def get_author(self):
        return self._author

    def display(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")


class Book(Publication):
    def __init__(self, title, author, num_of_pages):
        super().__init__(title, author)
        self.set_num_of_pages(num_of_pages)

    def set_num_of_pages(self, num_of_pages):
        if num_of_pages <= 0:
            print("The number of pages must be positive")
            self._num_of_pages = 0
        else:
            self._num_of_pages = num_of_pages

    def get_num_of_pages(self):
        return self._num_of_pages

    def display(self):
        super().display()
        print(f"Number of pages: {self._num_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_num):
        super().__init__(title, author)
        self.set_issue_num(issue_num)

    def set_issue_num(self, issue_num):
        if issue_num <= 0:
            print("The issue number must be positive")
            self._issue_num = 0
        else:
            self._issue_num = issue_num

    def get_issue_num(self):
        return self._issue_num

    def display(self):
        super().display()
        print(f"Issue number: {self._issue_num}")


pub1 = Publication("Journal of Experimental Psychology","Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
magazine1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display()

print("\nBook Information:")
book1.set_num_of_pages(310)
book1.display()

print("\nMagazine Information:")
magazine1.display()
