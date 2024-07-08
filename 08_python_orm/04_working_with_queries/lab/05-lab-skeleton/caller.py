import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Author, Book, Review


def find_books_by_genre_and_language(genre, language):
    return Book.objects.filter(genre=genre, language=language)


def find_authors_nationalities():
    authors_with_nationality = [
        f"{author.first_name} {author.last_name} is {author.nationality}"
        for author
        in Author.objects.filter(nationality__isnull=False)
    ]
    return "\n".join(authors_with_nationality)


def order_books_by_year():
    books_ordered = [
        f"{book.publication_year} year: {book.title} by {book.author}"
        for book
        in Book.objects.order_by("publication_year", "title")
    ]
    return "\n".join(books_ordered)


def delete_review_by_id(id):
    review_to_delete = Review.objects.get(id=id)
    review_to_delete.delete()
    return f"Review by {review_to_delete.reviewer_name} was deleted"


def filter_authors_by_nationalities(nationality):
    authors = Author.objects\
        .filter(nationality=nationality)\
        .order_by("first_name", "last_name")
    result = [
        author.biography
        if author.biography
        else str(author)
        for author in authors
    ]
    return "\n".join(result)


def filter_authors_by_birth_year(start, end):
    authors = Author.objects\
        .filter(birth_date__year__range=(start, end))\
        .order_by("-birth_date")
    return '\n'.join([
        f"{author.birth_date}: {author.first_name} {author.last_name}"
        for author
        in authors
    ])


def change_reviewer_name(name, new_name):
    Review.objects\
        .filter(reviewer_name=name)\
        .update(reviewer_name=new_name)
    return Review.objects.all()
