# # from models import db, User
# from models import db, Item, SpecialCategory
# from app import app  
# from datetime import datetime
# from faker import Faker

# fake = Faker()

# def seed_data():
#     groupthree_user = User(name="GroupThree", email="groupthree@gmail.com")
#     groupthree_user.password = "groupthreepassword"  # Set the password after initializing
    

#     # Add user to the session
#     db.session.add(groupthree_user)
#     db.session.commit() 
    
#     print("Database seeded successfully for GroupThree!")
# if __name__ == '__main__':
#     with app.app_context():
#         db.drop_all()  # Drops all tables (use with caution in production)
#         db.create_all()  # Creates all tables
#         seed_data()  # Calls the function to seed data
# # Create all tables in the database
# with app.app_context():
    
#     # User.query.delete()
#     Item.query.delete()
#     SpecialCategory.query.delete()

#     # print("Seeding users...")
    
#     # users = [
#     #     User(username= fake.name(), email= fake.email(), _password_hash= "password123"),
#     #     User(username= fake.name(), email= fake.email(), _password_hash= "passcode21"),
#     #     User(username= fake.name(), email= fake.email(), _password_hash= fake.word()),
#     #     User(username= fake.name(), email= fake.email(), _password_hash= "5faker10code"),
#     #     User(username= fake.name(), email= fake.email(), _password_hash= "access@123"),
#     #     User(username= fake.name(), email= fake.email(), _password_hash= fake.word())
#     # ]
    
#     # db.session.add_all(users)
    
#     # print("Users seeded successfully!")
    
#     print("Seeding items...")
    
#     items = [
#         Item(item_name= "Casual T-Shirt", description= "A comfortable and casual t-shirt for everyday wear.", price= 1999, category= "Clothes", items_available= 50, image_url= "Assets/clothes/black tshirt.jpeg"),
#         Item(item_name= "Classic Blue T-Shirt", description= "Stylish denim jacket with a classic fit.", price= 4999, category= "Clothes", items_available= 30, image_url= "/Assets/clothes/blue tshirt.jpeg"),
#         Item(item_name= "Classic Red T-Shirt", description= "Stylish denim jacket with a classic fit.", price= 3999, image_url= "/Assets/clothes/red tshirt.jpeg", category= "Clothes", items_available= 35),
#         Item(item_name= "The Great Gatsby by F. Scott Fitzgerald", price= 1099, category= "Books", items_available= 33, image_url= "https://covers.openlibrary.org/b/id/7222166-L.jpg"),
#         Item(item_name= "1984 by George Orwell", price= 999, category= "Books", items_available= 20, image_url= "https://covers.openlibrary.org/b/id/7222166-L.jpg"),
#         Item(item_name= "To Kill a Mockingbird by Harper Lee", price= 899, category= "Books", items_available= 42, image_url= "https://covers.openlibrary.org/b/id/8226191-L.jpg"),
#         Item(item_name= "Pride and Prejudice by Jane Austen", price= 799, category= "Books", items_available= 39, image_url= "https://covers.openlibrary.org/b/id/10525944-L.jpg"),
#         Item(item_name= "The Catcher in the Rye by J.D. Salinger", price= 1199, category= "Books", items_available= 19, image_url= "https://covers.openlibrary.org/b/id/8220281-L.jpg"),
#         Item(item_name= "Brave New World by Aldous Huxley", price= 1299, category= "Books", items_available= 45, image_url= "https://covers.openlibrary.org/b/id/10526109-L.jpg"),
#         Item(item_name= "Starry Night by Vincent van Gogh", price= 1999, category= "Artworks", items_available= 10, image_url= "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"),
#         Item(item_name= "Mona Lisa by Leonardo da Vinci", price= 2999, category= "Artworks", items_available= 15, image_url= "https://cdn.britannica.com/24/189624-050-F3C5BAA9/Mona-Lisa-oil-wood-panel-Leonardo-da.jpg?w=300&h=169&c=crop"),
#         Item(item_name= "Persistence of Memory by Salvador Dalí", price= 2499, category= "Artworks", items_available= 12, image_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKUU7NhqqGvyHudzEQhCLoaY905SyQTRv8QQ&s"),
#         Item(item_name= "The Scream by Edvard Munch", price= 3499, category= "Artworks", items_available= 8, image_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGBvPibMUi_tDxkc57g-177JGzae2Mhr0wjg&s"),
#         Item(item_name= "Girl with a Pearl Earring by Johannes Vermeer", price= 2999, category= "Artworks", items_available= 9, image_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIpTqXTG-qLkAqscLDvbq4eiAt4mBHAwJWnQ&s"),
#         Item(item_name= "The Birth of Venus by Sandro Botticelli", price= 3999, category= "Artworks", items_available= 10, image_url= "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg/800px-Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg"),
#         Item(item_name= "Running Shoes", price= 2000, category= "Shoes", items_available= 22, image_url= "/images/RS.jpeg"),
#         Item(item_name= "Casual Shoes", price= 9500, category= "Shoes", items_available= 30, image_url= "/images/CS.webp"),
#         Item(item_name= "Formal Shoes", price= 6000, category= "Shoes", items_available= 22, image_url= "/images/FS.jpg"),
#         Item(item_name= "Sneakers", price= 5500, category= "Shoes", items_available= 26, image_url= "/images/Sneakers.jpg"),
#         Item(item_name= "Boots", price= 5000, category= "Shoes", items_available= 17, image_url= "/images/Boots.jpg"),
#         Item(item_name= "OnePlus Vortex 9 Smartphone", price= 35000, category= "Electronics", items_available= 12, image_url= "/images/SP.webp"),
#         Item(item_name= "ZenBook Pro 14 Laptop", price= 60000, category= "Electronics", items_available= 19, image_url= "/images/LP.webp"),
#         Item(item_name= "BassBoost Wireless 4 Headphones", price= 5000, category= "Electronics", items_available= 10, image_url= "/images/HP.jpg"),
#         Item(item_name= "FitTrack Pro 3 Smartwatch", price= 12000, category= "Electronics", items_available= 15, image_url= "/images/SW.webp"),
#         Item(item_name= "TabMaster X10 Tablet", price= 22000, category= "Electronics", items_available= 14, image_url= "/images/Tablet.jpg"),
#         Item(item_name= "Blue Jeans", description= "Classic blue jeans with a modern fit.", price= 3999, category= "Clothes", items_available= 17, image_url= "Assets/whatsnew/Blue jeans.jpeg"),
#         Item(item_name= "White Sneakers", description= "Comfortable and stylish sneakers.", price= 5999, category= "Shoes", items_available= 18, image_url= "/Assets/whatsnew/Fashion men sneakers.jpeg"),
#         Item(item_name= "Hoodie", description= "Soft and warm Hoodie.", price= 4500, category= "Clothes", items_available= 31, image_url= "/Assets/whatsnew/Grey hoodie.jpeg"),
#         Item(item_name= "Classic Fit Polo Shirt", price= 3999, category= "Clothes", items_available= 21, offer_price= 2599, image_url= "/images/Classic Fit Polo Shirt.jpg"),
#         Item(item_name= "Women's Ankle Boots", price= 6999, category= "Shoes", items_available= 22, offer_price= 3999, image_url= "/images/Women's Ankle Boots.jpg"),
#         Item(item_name= "Atomic Habits by James Clear", price= 1899, category= "Books", items_available= 30, offer_price= 1199, image_url= "/images/'Atomic Habits' by James Clear.jpg"),
#         Item(item_name= "Abstract Canvas Painting", price= 9999, category= "Artwork", items_available= 11, offer_price= 6399, image_url= "/images/Abstract Canvas Painting.jpg"),
#         Item(item_name= "Wireless Bluetooth Earbuds", price= 5699, category= "Electronics", items_available= 18, offer_price= 2999, image_url= "/images/Wireless Bluetooth Earbuds.jpg"),
#         Item(item_name= "Maxi Dress with Floral Print", price= 5999, category= "Clothes", items_available= 7, offer_price= 3499, image_url= "/images/Maxi Dress with Floral Print.jpg"),
#         Item(item_name= "Becoming by Michelle Obama", price= 2499, category= "Books", items_available= 10, offer_price= 1599, image_url= "/images/'Becoming' by Michelle Obama.jpg"),
#         Item(item_name= "Smartwatch with Fitness Tracker", price= 12999, category= "Electronics", items_available= 12, offer_price= 6999, image_url= "/images/Smartwatch with Fitness Tracker.jpg"),
#         Item(item_name= "Handcrafted Ceramic Sculpture", price= 4499, category= "Artwork", items_available= 5, offer_price= 7999, image_url= "/images/Handcrafted Ceramic Sculpture.jpg"),
#         Item(item_name= "Leather Oxford Shoes", price= 5499, category= "Shoes", items_available= 11, image_url= "/images/Leather Oxford Shoes.jpg"),
#         Item(item_name= "Psychology of Money by Morgan Housel", price= 1999, category= "Books", items_available= 20, image_url= "/images/The Psychology of Money by Morgan Housel.jpg"),
#         Item(item_name= "Men's Slim Fit Chinos", price= 6799, category= "Clothes", items_available= 23, image_url= "/images/Men's Slim Fit Chinos.jpg"),
#         Item(item_name= "Digital Camera", price= 49999, category= "Electronics", items_available= 8, image_url= "/images/Digital Camera.jpg"),
#         Item(item_name= "Laptop Backpack", price= 5899, category= "Electronics", items_available= 11, image_url= "/images/Laptop Backpack.jpg"),
#         Item(item_name= "Women's Espadrille Wedges", price= 4899, category= "Shoes", items_available= 15, image_url= "/images/Women's Espadrille Wedges.jpg"),
#         Item(item_name= "The Alchemist by Paulo Coelho", price= 1499, category= "Books", items_available= 29, image_url= "/images/The Alchemist by Paulo Coelho.jpg"),
#         Item(item_name= "Modern Geometric Wall Art", price= 8199, category= "Artwork", items_available= 30, image_url= "/images/Modern Geometric Wall Art.jpg"),
#         Item(item_name= "White Leather Sneakers", price= 7599, category= "Shoes", items_available= 5, image_url= "/images/White Leather Sneakers.jpg"),
#         Item(item_name= "Subtle Art of Not Giving a F*ck by Mark Manson", price= 1799, category= "Books", items_available= 9, image_url= "/images/Subtle Art of Not giving a F.jpg"),
#         Item(item_name= "Men's Running Sneakers", price= 8999, category= "Shoes", items_available= 31, offer_price= 4999, image_url= "/images/Men's Running Sneakers.jpg")
#     ]
    
#     db.session.add_all(items)
    
#     print("Items seeded successfully!")
    
    
#     print("Seeding special categories...")
    
#     special_categories = [
#         SpecialCategory(name= "flash_sale"),
#         SpecialCategory(name= "hot_in_category"),
#         SpecialCategory(name= "whats_new")
#     ]
    
#     db.session.add_all(special_categories)
    
#     print("Special categories seeded successfully!")
    

#     # Commit the session to save the cart items
#     db.session.commit()

#     print("Database seeded successfully!")
    

from yourapp.models import Item 
from yourapp import db  

# Define your seed items
items = [ Item(item_name= "Casual T-Shirt", description= "A comfortable and casual t-shirt for everyday wear.", price= 1999, category= "Clothes", items_available= 50, image_url= "Assets/clothes/black tshirt.jpeg"),
        Item(item_name= "Classic Blue T-Shirt", description= "Stylish denim jacket with a classic fit.", price= 4999, category= "Clothes", items_available= 30, image_url= "/Assets/clothes/blue tshirt.jpeg"),
        Item(item_name= "Classic Red T-Shirt", description= "Stylish denim jacket with a classic fit.", price= 3999, image_url= "/Assets/clothes/red tshirt.jpeg", category= "Clothes", items_available= 35),
        Item(item_name= "The Great Gatsby by F. Scott Fitzgerald", price= 1099, category= "Books", items_available= 33, image_url= "https://covers.openlibrary.org/b/id/7222166-L.jpg"),
        Item(item_name= "1984 by George Orwell", price= 999, category= "Books", items_available= 20, image_url= "https://covers.openlibrary.org/b/id/7222166-L.jpg"),
        Item(item_name= "To Kill a Mockingbird by Harper Lee", price= 899, category= "Books", items_available= 42, image_url= "https://covers.openlibrary.org/b/id/8226191-L.jpg"),
        Item(item_name= "Pride and Prejudice by Jane Austen", price= 799, category= "Books", items_available= 39, image_url= "https://covers.openlibrary.org/b/id/10525944-L.jpg"),
        Item(item_name= "The Catcher in the Rye by J.D. Salinger", price= 1199, category= "Books", items_available= 19, image_url= "https://covers.openlibrary.org/b/id/8220281-L.jpg"),
        Item(item_name= "Brave New World by Aldous Huxley", price= 1299, category= "Books", items_available= 45, image_url= "https://covers.openlibrary.org/b/id/10526109-L.jpg"),
        Item(item_name= "Starry Night by Vincent van Gogh", price= 1999, category= "Artworks", items_available= 10, image_url= "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1200px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"),
        Item(item_name= "Mona Lisa by Leonardo da Vinci", price= 2999, category= "Artworks", items_available= 15, image_url= "https://cdn.britannica.com/24/189624-050-F3C5BAA9/Mona-Lisa-oil-wood-panel-Leonardo-da.jpg?w=300&h=169&c=crop"),
        Item(item_name= "Persistence of Memory by Salvador Dalí", price= 2499, category= "Artworks", items_available= 12, image_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKUU7NhqqGvyHudzEQhCLoaY905SyQTRv8QQ&s"),
        Item(item_name= "The Scream by Edvard Munch", price= 3499, category= "Artworks", items_available= 8, image_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGBvPibMUi_tDxkc57g-177JGzae2Mhr0wjg&s"),
        Item(item_name= "Girl with a Pearl Earring by Johannes Vermeer", price= 2999, category= "Artworks", items_available= 9, image_url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIpTqXTG-qLkAqscLDvbq4eiAt4mBHAwJWnQ&s"),
        Item(item_name= "The Birth of Venus by Sandro Botticelli", price= 3999, category= "Artworks", items_available= 10, image_url= "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg/800px-Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg"),
        Item(item_name= "Running Shoes", price= 2000, category= "Shoes", items_available= 22, image_url= "/images/RS.jpeg"),
        Item(item_name= "Casual Shoes", price= 9500, category= "Shoes", items_available= 30, image_url= "/images/CS.webp"),
        Item(item_name= "Formal Shoes", price= 6000, category= "Shoes", items_available= 22, image_url= "/images/FS.jpg"),
        Item(item_name= "Sneakers", price= 5500, category= "Shoes", items_available= 26, image_url= "/images/Sneakers.jpg"),
        Item(item_name= "Boots", price= 5000, category= "Shoes", items_available= 17, image_url= "/images/Boots.jpg"),
        Item(item_name= "OnePlus Vortex 9 Smartphone", price= 35000, category= "Electronics", items_available= 12, image_url= "/images/SP.webp"),
        Item(item_name= "ZenBook Pro 14 Laptop", price= 60000, category= "Electronics", items_available= 19, image_url= "/images/LP.webp"),
        Item(item_name= "BassBoost Wireless 4 Headphones", price= 5000, category= "Electronics", items_available= 10, image_url= "/images/HP.jpg"),
        Item(item_name= "FitTrack Pro 3 Smartwatch", price= 12000, category= "Electronics", items_available= 15, image_url= "/images/SW.webp"),
        Item(item_name= "TabMaster X10 Tablet", price= 22000, category= "Electronics", items_available= 14, image_url= "/images/Tablet.jpg"),
        Item(item_name= "Blue Jeans", description= "Classic blue jeans with a modern fit.", price= 3999, category= "Clothes", items_available= 17, image_url= "Assets/whatsnew/Blue jeans.jpeg"),
        Item(item_name= "White Sneakers", description= "Comfortable and stylish sneakers.", price= 5999, category= "Shoes", items_available= 18, image_url= "/Assets/whatsnew/Fashion men sneakers.jpeg"),
        Item(item_name= "Hoodie", description= "Soft and warm Hoodie.", price= 4500, category= "Clothes", items_available= 31, image_url= "/Assets/whatsnew/Grey hoodie.jpeg"),
        Item(item_name= "Classic Fit Polo Shirt", price= 3999, category= "Clothes", items_available= 21, offer_price= 2599, image_url= "/images/Classic Fit Polo Shirt.jpg"),
        Item(item_name= "Women's Ankle Boots", price= 6999, category= "Shoes", items_available= 22, offer_price= 3999, image_url= "/images/Women's Ankle Boots.jpg"),
        Item(item_name= "Atomic Habits by James Clear", price= 1899, category= "Books", items_available= 30, offer_price= 1199, image_url= "/images/'Atomic Habits' by James Clear.jpg"),
        Item(item_name= "Abstract Canvas Painting", price= 9999, category= "Artwork", items_available= 11, offer_price= 6399, image_url= "/images/Abstract Canvas Painting.jpg"),
        Item(item_name= "Wireless Bluetooth Earbuds", price= 5699, category= "Electronics", items_available= 18, offer_price= 2999, image_url= "/images/Wireless Bluetooth Earbuds.jpg"),
        Item(item_name= "Maxi Dress with Floral Print", price= 5999, category= "Clothes", items_available= 7, offer_price= 3499, image_url= "/images/Maxi Dress with Floral Print.jpg"),
        Item(item_name= "Becoming by Michelle Obama", price= 2499, category= "Books", items_available= 10, offer_price= 1599, image_url= "/images/'Becoming' by Michelle Obama.jpg"),
        Item(item_name= "Smartwatch with Fitness Tracker", price= 12999, category= "Electronics", items_available= 12, offer_price= 6999, image_url= "/images/Smartwatch with Fitness Tracker.jpg"),
        Item(item_name= "Handcrafted Ceramic Sculpture", price= 4499, category= "Artwork", items_available= 5, offer_price= 7999, image_url= "/images/Handcrafted Ceramic Sculpture.jpg"),
        Item(item_name= "Leather Oxford Shoes", price= 5499, category= "Shoes", items_available= 11, image_url= "/images/Leather Oxford Shoes.jpg"),
        Item(item_name= "Psychology of Money by Morgan Housel", price= 1999, category= "Books", items_available= 20, image_url= "/images/The Psychology of Money by Morgan Housel.jpg"),
        Item(item_name= "Men's Slim Fit Chinos", price= 6799, category= "Clothes", items_available= 23, image_url= "/images/Men's Slim Fit Chinos.jpg"),
        Item(item_name= "Digital Camera", price= 49999, category= "Electronics", items_available= 8, image_url= "/images/Digital Camera.jpg"),
        Item(item_name= "Laptop Backpack", price= 5899, category= "Electronics", items_available= 11, image_url= "/images/Laptop Backpack.jpg"),
        Item(item_name= "Women's Espadrille Wedges", price= 4899, category= "Shoes", items_available= 15, image_url= "/images/Women's Espadrille Wedges.jpg"),
        Item(item_name= "The Alchemist by Paulo Coelho", price= 1499, category= "Books", items_available= 29, image_url= "/images/The Alchemist by Paulo Coelho.jpg"),
        Item(item_name= "Modern Geometric Wall Art", price= 8199, category= "Artwork", items_available= 30, image_url= "/images/Modern Geometric Wall Art.jpg"),
        Item(item_name= "White Leather Sneakers", price= 7599, category= "Shoes", items_available= 5, image_url= "/images/White Leather Sneakers.jpg"),
        Item(item_name= "Subtle Art of Not Giving a F*ck by Mark Manson", price= 1799, category= "Books", items_available= 9, image_url= "/images/Subtle Art of Not giving a F.jpg"),
        Item(item_name= "Men's Running Sneakers", price= 8999, category= "Shoes", items_available= 31, offer_price= 4999, image_url= "/images/Men's Running Sneakers.jpg")
]

# Seed data into your database
def seed_items():
    for item in items:
        # Assuming 'product_quantity' is a field in your database model that maps to 'items_available'
        product = Item(
            item_name=item.item_name,
            description=item.description,
            price=item.price,
            category=item.category,
            product_quantity=item.items_available,  # Use items_available to seed product_quantity
            image_url=item.image_url
        )
        
        db.session.add(product)
    
    db.session.commit()  # Save changes to the database

# Run the seed function
if __name__ == "__main__":
    seed_items()




