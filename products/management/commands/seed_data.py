# products/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Seeds the database with sample products'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        # Create categories
        categories_data = [
            {'name': 'Electronics', 'slug': 'electronics'},
            {'name': 'Clothing', 'slug': 'clothing'},
            {'name': 'Books', 'slug': 'books'},
            {'name': 'Home & Garden', 'slug': 'home-garden'},
            {'name': 'Sports', 'slug': 'sports'},
            {'name': 'Beauty', 'slug': 'beauty'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            categories[cat_data['slug']] = category
            self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
        
        # Create sample products
        products_data = [
            {
                'name': 'iPhone 14 Pro',
                'slug': 'iphone-14-pro',
                'category': categories['electronics'],
                'price': 999.99,
                'description': 'Latest iPhone with advanced camera system, A16 Bionic chip, and Dynamic Island.',
            },
            {
                'name': 'Samsung Galaxy S23',
                'slug': 'samsung-galaxy-s23',
                'category': categories['electronics'],
                'price': 799.99,
                'description': 'Powerful Android smartphone with professional-grade camera and Snapdragon processor.',
            },
            {
                'name': 'Sony Headphones WH-1000XM5',
                'slug': 'sony-headphones-wh1000xm5',
                'category': categories['electronics'],
                'price': 399.99,
                'description': 'Industry-leading noise cancellation with premium sound quality and 30-hour battery.',
            },
            {
                'name': 'Men\'s Casual Shirt',
                'slug': 'mens-casual-shirt',
                'category': categories['clothing'],
                'price': 29.99,
                'description': 'Comfortable cotton shirt perfect for casual wear. Available in multiple colors.',
            },
            {
                'name': 'Women\'s Summer Dress',
                'slug': 'womens-summer-dress',
                'category': categories['clothing'],
                'price': 49.99,
                'description': 'Lightweight and breezy dress perfect for summer days. Floral pattern available.',
            },
            {
                'name': 'Python Crash Course',
                'slug': 'python-crash-course',
                'category': categories['books'],
                'price': 34.99,
                'description': 'A hands-on, project-based introduction to programming. Best for beginners.',
            },
            {
                'name': 'The Lean Startup',
                'slug': 'the-lean-startup',
                'category': categories['books'],
                'price': 24.99,
                'description': 'How constant innovation creates radically successful businesses.',
            },
            {
                'name': 'Coffee Maker',
                'slug': 'coffee-maker',
                'category': categories['home-garden'],
                'price': 89.99,
                'description': 'Programmable coffee maker with thermal carafe and built-in grinder.',
            },
            {
                'name': 'Yoga Mat',
                'slug': 'yoga-mat',
                'category': categories['sports'],
                'price': 24.99,
                'description': 'Non-slip yoga mat with carrying strap. Eco-friendly materials.',
            },
            {
                'name': 'Basketball',
                'slug': 'basketball',
                'category': categories['sports'],
                'price': 29.99,
                'description': 'Official size and weight basketball with durable rubber construction.',
            },
            {
                'name': 'Skincare Set',
                'slug': 'skincare-set',
                'category': categories['beauty'],
                'price': 59.99,
                'description': 'Complete skincare routine with cleanser, toner, and moisturizer.',
            },
            {
                'name': 'Laptop Backpack',
                'slug': 'laptop-backpack',
                'category': categories['electronics'],
                'price': 49.99,
                'description': 'Water-resistant backpack with laptop compartment and multiple pockets.',
            },
        ]
        
        for product_data in products_data:
            product = Product.objects.create(**product_data)
            self.stdout.write(self.style.SUCCESS(f'Created product: {product.name} - ${product.price}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database with sample data!'))