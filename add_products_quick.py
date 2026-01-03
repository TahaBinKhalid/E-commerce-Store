# add_50_real_products.py
import os
import django
from decimal import Decimal
from datetime import datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estore.settings')
django.setup()

from products.models import Category, Product

def get_placeholder_image_url(product_name, category):
    """Generate a reliable placeholder image URL based on product name and category"""
    # Clean the product name for URL
    clean_name = product_name.replace(' ', '+').replace('&', 'and')
    
    # Color scheme based on category
    colors = {
        "electronics": ("1e3a8a", "ffffff"),  # Blue
        "clothing": ("1e40af", "ffffff"),    # Light blue
        "books": ("059669", "ffffff"),       # Green
        "home-kitchen": ("7c3aed", "ffffff"), # Purple
        "sports-outdoors": ("f59e0b", "ffffff"), # Amber
        "beauty-health": ("db2777", "ffffff"), # Pink
    }
    
    bg_color, text_color = colors.get(category, ("3b82f6", "ffffff"))
    
    # Use placeholder.co - 100% reliable
    return f"https://placehold.co/600x400/{bg_color}/{text_color}.png?text={clean_name}"

PRODUCTS_DATA = [
    # ============ ELECTRONICS ============
    {
        "category": "Electronics",
        "category_slug": "electronics",
        "products": [
            {
                "name": "iPhone 15 Pro Max",
                "slug": "iphone-15-pro-max",
                "price": 1199.99,
                "description": "Apple's latest flagship with A17 Pro chip, titanium design, 48MP main camera, and Dynamic Island. Features 6.7-inch Super Retina XDR display, 5x optical zoom, and USB-C connectivity.",
            },
            {
                "name": "Samsung Galaxy S24 Ultra",
                "slug": "samsung-galaxy-s24-ultra",
                "price": 1299.99,
                "description": "AI-powered smartphone with S Pen, 200MP camera system, Snapdragon 8 Gen 3 processor, and 6.8-inch Dynamic AMOLED 2X display. Titanium frame with Gorilla Glass Armor.",
            },
            {
                "name": "MacBook Pro 16-inch M3 Max",
                "slug": "macbook-pro-16-m3-max",
                "price": 3499.99,
                "description": "Professional laptop with M3 Max chip, 16-core CPU, 40-core GPU, 48GB unified memory. Liquid Retina XDR display with ProMotion. Perfect for video editing and 3D rendering.",
            },
            {
                "name": "Sony WH-1000XM5 Headphones",
                "slug": "sony-wh-1000xm5-headphones",
                "price": 399.99,
                "description": "Premium wireless noise-cancelling headphones with 30-hour battery life, 8 microphones for crystal clear calls, and Adaptive Sound Control. Multiple noise cancellation levels.",
            },
            {
                "name": "Apple Watch Series 9",
                "slug": "apple-watch-series-9",
                "price": 429.99,
                "description": "Smartwatch with S9 SiP chip, always-on retina display, blood oxygen sensor, ECG app. New double tap gesture control. Aluminum or stainless steel case options.",
            },
            {
                "name": "Sony PlayStation 5",
                "slug": "sony-playstation-5",
                "price": 499.99,
                "description": "Next-gen gaming console with 4K/120fps gaming, ray tracing, 825GB SSD storage. Includes DualSense wireless controller with haptic feedback and adaptive triggers.",
            },
            {
                "name": "DJI Mini 4 Pro Drone",
                "slug": "dji-mini-4-pro-drone",
                "price": 759.99,
                "description": "Ultra-light camera drone with 4K/60fps video, 48MP photos, omnidirectional obstacle sensing, 34-min flight time. Includes 3-axis gimbal and advanced tracking features.",
            },
            {
                "name": "Canon EOS R5 Camera",
                "slug": "canon-eos-r5-camera",
                "price": 3899.99,
                "description": "Full-frame mirrorless camera with 45MP sensor, 8K video recording, 20fps continuous shooting. In-body image stabilization up to 8 stops. Dual pixel CMOS AF II.",
            },
            {
                "name": "iPad Pro 12.9-inch M2",
                "slug": "ipad-pro-12-9-m2",
                "price": 1099.99,
                "description": "Pro tablet with M2 chip, Liquid Retina XDR display with ProMotion, 12MP front camera with Center Stage. Supports Apple Pencil hover feature and Magic Keyboard.",
            },
            {
                "name": "Meta Quest 3 VR Headset",
                "slug": "meta-quest-3-vr",
                "price": 499.99,
                "description": "Mixed reality headset with pancake lenses, 4K+ resolution per eye, Snapdragon XR2 Gen 2 chip. Passthrough with full-color 3D depth sensors. 128GB storage.",
            },
            {
                "name": "Bose QuietComfort Ultra",
                "slug": "bose-quietcomfort-ultra",
                "price": 429.99,
                "description": "Wireless headphones with Immersive Audio technology, CustomTune sound calibration, world-class noise cancellation. Up to 24 hours battery life with quick charge.",
            },
            {
                "name": "Samsung 85-inch 4K QLED TV",
                "slug": "samsung-85-inch-4k-qled",
                "price": 2199.99,
                "description": "Quantum HDR with Quantum Matrix Technology, Object Tracking Sound, Gaming Hub with 4K 144Hz. Smart TV with Alexa and Google Assistant built-in.",
            },
            {
                "name": "Microsoft Surface Laptop 5",
                "slug": "microsoft-surface-laptop-5",
                "price": 1299.99,
                "description": "13.5-inch PixelSense touchscreen, Intel Core i7, 16GB RAM, 512GB SSD. Premium aluminum build with omnisonic speakers and Dolby Atmos support.",
            },
            {
                "name": "GoPro HERO12 Black",
                "slug": "gopro-hero12-black",
                "price": 399.99,
                "description": "Action camera with 5.3K60 video, 27MP photos, HyperSmooth 6.0 stabilization, 177-degree field of view. Waterproof to 33ft without housing.",
            },
            {
                "name": "Nintendo Switch OLED",
                "slug": "nintendo-switch-oled",
                "price": 349.99,
                "description": "Gaming console with 7-inch OLED screen, enhanced audio, 64GB internal storage. Includes adjustable wide stand and dock with wired LAN port.",
            },
        ]
    },
    
    # ============ CLOTHING & FASHION ============
    {
        "category": "Clothing",
        "category_slug": "clothing",
        "products": [
            {
                "name": "Premium Cotton T-Shirt",
                "slug": "premium-cotton-t-shirt",
                "price": 24.99,
                "description": "100% organic cotton crew neck t-shirt. Pre-shrunk fabric, double-stitched hem, and tear-away label for comfort. Available in 10 colors.",
            },
            {
                "name": "Men's Casual Button-Down Shirt",
                "slug": "mens-casual-button-down-shirt",
                "price": 49.99,
                "description": "Classic fit button-down shirt in breathable cotton-poplin. Spread collar, button cuffs, and curved hem. Perfect for business casual or weekend wear.",
            },
            {
                "name": "Women's Floral Summer Dress",
                "slug": "womens-floral-summer-dress",
                "price": 69.99,
                "description": "Lightweight midi dress with floral pattern, smocked bodice, and flutter sleeves. Made from breathable viscose with lining. Perfect for warm weather occasions.",
            },
            {
                "name": "Nike Air Max 270",
                "slug": "nike-air-max-270",
                "price": 159.99,
                "description": "Casual sneakers with the largest Air Max unit ever. Breathable mesh upper, foam midsole, and rubber outsole. Max Air cushioning for all-day comfort.",
            },
            {
                "name": "Leather Bomber Jacket",
                "slug": "leather-bomber-jacket",
                "price": 299.99,
                "description": "Genuine leather jacket with ribbed knit collar, cuffs and hem. Zipper closure, multiple pockets, and quilted lining for warmth and style.",
            },
            {
                "name": "Designer Denim Jeans",
                "slug": "designer-denim-jeans",
                "price": 89.99,
                "description": "Premium stretch denim jeans with slim fit, five-pocket styling, and contrast stitching. Made from sustainable cotton with elastane for comfort.",
            },
            {
                "name": "Cashmere Sweater",
                "slug": "cashmere-sweater",
                "price": 199.99,
                "description": "100% pure cashmere crew neck sweater. Ultra-soft, lightweight, and warm. Ribbed trim at neck, cuffs and hem. Hand wash recommended.",
            },
            {
                "name": "Active Wear Hoodie",
                "slug": "active-wear-hoodie",
                "price": 59.99,
                "description": "Performance hoodie with moisture-wicking fabric, kangaroo pocket, and adjustable hood. Perfect for workouts or casual wear.",
            },
            {
                "name": "Silk Scarf",
                "slug": "silk-scarf",
                "price": 79.99,
                "description": "100% silk square scarf with hand-rolled edges. 35x35 inches with vibrant floral pattern. Can be worn as headscarf, neck scarf, or bag accessory.",
            },
            {
                "name": "Wool Blend Coat",
                "slug": "wool-blend-coat",
                "price": 249.99,
                "description": "Double-breasted wool blend coat with notch lapel, button closure, and internal pocket. Fully lined with functional sleeve buttons.",
            },
        ]
    },
    
    # ============ BOOKS & MEDIA ============
    {
        "category": "Books",
        "category_slug": "books",
        "products": [
            {
                "name": "Python Crash Course 3rd Edition",
                "slug": "python-crash-course-3rd",
                "price": 39.99,
                "description": "Best-selling Python book with hands-on projects. Covers Python basics, web development with Django, data visualization, and game development.",
            },
            {
                "name": "Clean Code: A Handbook",
                "slug": "clean-code-handbook",
                "price": 44.99,
                "description": "Essential reading for software developers. Covers principles, patterns, and practices for writing clean, maintainable code.",
            },
            {
                "name": "Atomic Habits",
                "slug": "atomic-habits",
                "price": 27.99,
                "description": "James Clear's practical guide to building good habits and breaking bad ones. Tiny changes lead to remarkable results.",
            },
            {
                "name": "The Psychology of Money",
                "slug": "psychology-of-money",
                "price": 22.99,
                "description": "Timeless lessons on wealth, greed, and happiness. How to make better financial decisions and understand the psychological aspects of money.",
            },
            {
                "name": "Django for Professionals",
                "slug": "django-for-professionals",
                "price": 49.99,
                "description": "Build powerful, secure web applications with Django and Python. Covers Docker, PostgreSQL, authentication, permissions, and deployment.",
            },
        ]
    },
    
    # ============ HOME & KITCHEN ============
    {
        "category": "Home & Kitchen",
        "category_slug": "home-kitchen",
        "products": [
            {
                "name": "Stainless Steel Cookware Set",
                "slug": "stainless-steel-cookware-set",
                "price": 299.99,
                "description": "10-piece cookware set with triple-ply construction, even heat distribution, and oven-safe up to 500°F. Includes pots, pans, and lids.",
            },
            {
                "name": "Memory Foam Mattress",
                "slug": "memory-foam-mattress",
                "price": 799.99,
                "description": "12-inch gel memory foam mattress with CertiPUR-US certified foam. Pressure-relieving, breathable, and hypoallergenic. 100-night trial.",
            },
            {
                "name": "Robot Vacuum Cleaner",
                "slug": "robot-vacuum-cleaner",
                "price": 349.99,
                "description": "Smart mapping robot vacuum with self-emptying base, obstacle avoidance, and mopping function. Works with Alexa and Google Assistant.",
            },
            {
                "name": "Air Purifier with HEPA Filter",
                "slug": "air-purifier-hepa",
                "price": 199.99,
                "description": "Covers up to 500 sq ft, removes 99.97% of allergens, pollutants, and odors. Smart sensor adjusts fan speed automatically.",
            },
        ]
    },
    
    # ============ SPORTS & OUTDOORS ============
    {
        "category": "Sports & Outdoors",
        "category_slug": "sports-outdoors",
        "products": [
            {
                "name": "Mountain Bike",
                "slug": "mountain-bike",
                "price": 899.99,
                "description": "27.5-inch hardtail mountain bike with aluminum frame, 21-speed Shimano drivetrain, hydraulic disc brakes, and suspension fork.",
            },
            {
                "name": "Yoga Mat Premium",
                "slug": "yoga-mat-premium",
                "price": 34.99,
                "description": "Eco-friendly yoga mat with double-sided non-slip surface, 6mm thickness for joint protection, and alignment markers. Includes carrying strap.",
            },
            {
                "name": "Camping Tent 4-Person",
                "slug": "camping-tent-4-person",
                "price": 149.99,
                "description": "Waterproof dome tent with fiberglass poles, rain fly, and mesh windows. Sets up in 10 minutes. Includes carrying bag and stakes.",
            },
            {
                "name": "Fitness Tracker Watch",
                "slug": "fitness-tracker-watch",
                "price": 129.99,
                "description": "Tracks heart rate, sleep, steps, calories burned. Water-resistant, 7-day battery, GPS, and smartphone notifications.",
            },
        ]
    },
    
    # ============ BEAUTY & HEALTH ============
    {
        "category": "Beauty & Health",
        "category_slug": "beauty-health",
        "products": [
            {
                "name": "Professional Hair Dryer",
                "slug": "professional-hair-dryer",
                "price": 199.99,
                "description": "Ionic hair dryer with 1875 watts, 3 heat/2 speed settings, concentrator nozzle, and diffuser. Reduces frizz and drying time.",
            },
            {
                "name": "Skincare Set",
                "slug": "skincare-set",
                "price": 89.99,
                "description": "Complete skincare routine: cleanser, toner, serum, moisturizer, and SPF. All products are cruelty-free and vegan.",
            },
            {
                "name": "Electric Toothbrush",
                "slug": "electric-toothbrush",
                "price": 79.99,
                "description": "Sonic electric toothbrush with 4 modes, pressure sensor, and 2-week battery life. Includes travel case and multiple brush heads.",
            },
        ]
    },
]

# Extra products to reach 50+
EXTRA_PRODUCTS = [
    ("Wireless Earbuds Pro", 179.99, "True wireless earbuds with ANC"),
    ("Gaming Keyboard RGB", 129.99, "Mechanical keyboard with RGB lighting"),
    ("Smart Water Bottle", 49.99, "Tracks water intake with app"),
    ("Portable Blender", 59.99, "USB-C rechargeable smoothie maker"),
    ("Backpack with Solar Panel", 89.99, "Charges devices while hiking"),
    ("Noise Cancelling Earbuds", 149.99, "Compact earbuds with ANC"),
    ("Smart Light Bulbs Pack", 79.99, "4-pack color changing bulbs"),
    ("Electric Kettle Temperature Control", 89.99, "Variable temperature kettle"),
    ("Standing Desk Converter", 199.99, "Adjustable height desktop"),
    ("Wireless Charging Pad", 39.99, "15W fast charging for multiple devices"),
    ("Smart TV 55-inch", 699.99, "4K Smart TV with streaming apps"),
    ("Bluetooth Speaker", 89.99, "Portable speaker with 20h battery"),
    ("Wireless Mouse", 39.99, "Ergonomic wireless mouse"),
    ("External SSD 1TB", 129.99, "Fast external solid state drive"),
    ("Smart Home Hub", 99.99, "Control all smart home devices"),
    ("Electric Scooter", 499.99, "Foldable electric scooter"),
    ("Digital Camera", 599.99, "24MP digital camera with lens"),
    ("Gaming Mouse", 79.99, "High DPI gaming mouse"),
    ("Monitor 27-inch", 299.99, "4K computer monitor"),
    ("Tablet Stand", 29.99, "Adjustable tablet holder"),
]

def clear_database():
    """Clear all existing products and categories"""
    print("🧹 Clearing all existing products and categories...")
    Product.objects.all().delete()
    Category.objects.all().delete()
    print("   ✓ Database cleared")

def add_all_products():
    print("🚀 Adding 50+ Real Products to Your Store...")
    print("=" * 60)
    
    total_created = 0
    total_with_images = 0
    
    # Clear database first
    clear_database()
    
    # Add main products
    for category_data in PRODUCTS_DATA:
        category, created = Category.objects.get_or_create(
            name=category_data["category"],
            slug=category_data["category_slug"]
        )
        
        print(f"\n📁 {category.name}:")
        
        for product_data in category_data["products"]:
            try:
                # Generate placeholder image URL
                image_url = get_placeholder_image_url(
                    product_data["name"], 
                    category_data["category_slug"]
                )
                
                # Create product
                product = Product.objects.create(
                    category=category,
                    name=product_data["name"],
                    slug=product_data["slug"],
                    price=Decimal(str(product_data["price"])),
                    description=product_data["description"],
                    available=True,
                )
                
                # Set image URL directly (no download needed)
                product.image_url = image_url
                product.save()
                
                total_created += 1
                total_with_images += 1
                print(f"   ✓ {product.name} - ${product.price}")
                
            except Exception as e:
                print(f"   ✗ Error creating {product_data.get('name', 'unknown')}: {e}")
    
    # Add extra products to electronics category
    print(f"\n📦 Adding extra products to Electronics:")
    electronics = Category.objects.get(slug="electronics")
    
    for i, (name, price, desc) in enumerate(EXTRA_PRODUCTS, 1):
        try:
            # Generate placeholder image
            image_url = get_placeholder_image_url(name, "electronics")
            
            # Create product
            product = Product.objects.create(
                category=electronics,
                name=name,
                slug=f"extra-product-{i}",
                price=Decimal(str(price)),
                description=f"{desc}. Premium quality with warranty.",
                available=True,
            )
            
            # Set image URL
            product.image_url = image_url
            product.save()
            
            total_created += 1
            total_with_images += 1
            print(f"   ✓ {name} - ${price}")
            
        except Exception as e:
            print(f"   ✗ Error creating {name}: {e}")
    
    # Display final statistics
    print("\n" + "=" * 60)
    print("✅ COMPLETE!")
    print(f"📊 Total products created: {total_created}")
    print(f"📊 Total products with images: {total_with_images}")
    print(f"📊 Total in database: {Product.objects.count()}")
    print(f"📊 Total categories: {Category.objects.count()}")
    
    print("\n🎯 Category breakdown:")
    for category in Category.objects.all():
        count = Product.objects.filter(category=category).count()
        print(f"   • {category.name}: {count} products")
    
    print("\n🌐 Your store URLs:")
    print("   Home: http://127.0.0.1:8000/")
    print("   Products: http://127.0.0.1:8000/products/")
    print("   Admin: http://127.0.0.1:8000/admin/")
    
    print("\n💡 IMPORTANT: Update your templates to use image_url field")
    print("   In product_list.html, use: <img src='{{ product.image_url }}'>")
    print("   Instead of: <img src='{{ product.image.url }}'>")

if __name__ == "__main__":
    add_all_products()
    
    print("\n" + "=" * 60)
    print("🔥 Your e-commerce store is now ready with 50+ products!")
    print("\n📱 Test your store:")
    print("   1. Run: python manage.py runserver")
    print("   2. Visit: http://127.0.0.1:8000/")
    print("   3. All products will show placeholder images")
    print("\n⚠️  Note: Images are now stored as URLs, not downloaded files")
    print("   This ensures 100% reliability for all products")