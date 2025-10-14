from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from books.models import Author, Book, Member, BorrowRecord
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Clear existing data
        BorrowRecord.objects.all().delete()
        Member.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        # Create authors
        author1 = Author.objects.create(
            first_name="Machado",
            last_name="de Assis",
            birth_date=date(1839, 6, 21)
        )
        
        author2 = Author.objects.create(
            first_name="Jorge",
            last_name="Amado",
            birth_date=date(1912, 8, 10)
        )
        
        author3 = Author.objects.create(
            first_name="Paulo",
            last_name="Coelho",
            birth_date=date(1947, 8, 24)
        )

        # Create books
        book1 = Book.objects.create(
            title="Dom Casmurro",
            author=author1,
            isbn="9788525043731",
            publication_date=date(1899, 1, 1),
            pages=256,
            available=True
        )
        
        book2 = Book.objects.create(
            title="Memórias Póstumas de Brás Cubas",
            author=author1,
            isbn="9788525044776",
            publication_date=date(1881, 1, 1),
            pages=288,
            available=True
        )
        
        book3 = Book.objects.create(
            title="Capitães da Areia",
            author=author2,
            isbn="9788525044875",
            publication_date=date(1937, 1, 1),
            pages=320,
            available=False
        )
        
        book4 = Book.objects.create(
            title="O Alquimista",
            author=author3,
            isbn="9788575421079",
            publication_date=date(1988, 1, 1),
            pages=192,
            available=True
        )

        # Create users
        user1 = User.objects.create_user(
            username="joao_silva",
            first_name="João",
            last_name="Silva",
            email="joao@example.com",
            password="password123"
        )
        
        user2 = User.objects.create_user(
            username="maria_santos",
            first_name="Maria",
            last_name="Santos",
            email="maria@example.com",
            password="password123"
        )
        
        user3 = User.objects.create_user(
            username="pedro_costa",
            first_name="Pedro",
            last_name="Costa",
            email="pedro@example.com",
            password="password123"
        )

        # Create members
        member1 = Member.objects.create(
            user=user1,
            phone_number="(11) 99999-9999",
            is_active=True
        )
        
        member2 = Member.objects.create(
            user=user2,
            phone_number="(21) 98888-8888",
            is_active=True
        )
        
        member3 = Member.objects.create(
            user=user3,
            phone_number="(31) 97777-7777",
            is_active=False
        )

        # Create borrow records
        borrow1 = BorrowRecord.objects.create(
            book=book3,
            member=member1,
            borrow_date=date.today() - timedelta(days=15),
            return_date=None
        )
        
        borrow2 = BorrowRecord.objects.create(
            book=book1,
            member=member2,
            borrow_date=date.today() - timedelta(days=30),
            return_date=date.today() - timedelta(days=10)
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully populated the database with sample data\n'
                f'Authors: {Author.objects.count()}\n'
                f'Books: {Book.objects.count()}\n'
                f'Members: {Member.objects.count()}\n'
                f'Borrow Records: {BorrowRecord.objects.count()}'
            )
        )