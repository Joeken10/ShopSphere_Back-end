def user_serializer(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
       
    }
