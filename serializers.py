# serializers.py

def user_serializer(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "password": user.password
    }

def item_serializer(item):
    return {
        "id": item.id,
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "category": item.category,
        "items_available": item.items_available,
        "offer_price": item.offer_price,
        "image_url": item.image_url
    }
