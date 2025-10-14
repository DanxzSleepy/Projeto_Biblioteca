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
        
        # Only delete non-superuser users (keep superusers)
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

        # Create or get users
        user1, created = User.objects.get_or_create(
            username="joao_silva",
            defaults={
                'first_name': "João",
                'last_name': "Silva",
                'email': "joao@example.com"
            }
        )
        if created:
            user1.set_password("password123")
            user1.save()
        
        user2, created = User.objects.get_or_create(
            username="maria_santos",
            defaults={
                'first_name': "Maria",
                'last_name': "Santos",
                'email': "maria@example.com"
            }
        )
        if created:
            user2.set_password("password123")
            user2.save()
        
        user3, created = User.objects.get_or_create(
            username="pedro_costa",
            defaults={
                'first_name': "Pedro",
                'last_name': "Costa",
                'email': "pedro@example.com"
            }
        )
        if created:
            user3.set_password("password123")
            user3.save()
        
        # Create librarian user
        user4, created = User.objects.get_or_create(
            username="ana_bibliotecaria",
            defaults={
                'first_name': "Ana",
                'last_name': "Bibliotecária",
                'email': "ana@example.com"
            }
        )
        if created:
            user4.set_password("password123")
            user4.save()
        
        # Create admin user
        user5, created = User.objects.get_or_create(
            username="carlos_admin",
            defaults={
                'first_name': "Carlos",
                'last_name': "Administrador",
                'email': "carlos@example.com"
            }
        )
        if created:
            user5.set_password("password123")
            user5.save()

        # Create members
        member1, created = Member.objects.get_or_create(
            user=user1,
            defaults={
                'phone_number': "(11) 99999-9999",
                'is_active': True,
                'role': 'member'
            }
        )
        
        member2, created = Member.objects.get_or_create(
            user=user2,
            defaults={
                'phone_number': "(21) 98888-8888",
                'is_active': True,
                'role': 'member'
            }
        )
        
        member3, created = Member.objects.get_or_create(
            user=user3,
            defaults={
                'phone_number': "(31) 97777-7777",
                'is_active': False,
                'role': 'member'
            }
        )
        
        # Create librarian
        member4, created = Member.objects.get_or_create(
            user=user4,
            defaults={
                'phone_number': "(41) 96666-6666",
                'is_active': True,
                'role': 'librarian'
            }
        )
        
        # Create admin
        member5, created = Member.objects.get_or_create(
            user=user5,
            defaults={
                'phone_number': "(51) 95555-5555",
                'is_active': True,
                'role': 'admin'
            }
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