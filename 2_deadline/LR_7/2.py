def build_user_profile(user_id: int, **kwargs) -> dict:
    profile = {'user_id': user_id}
    profile.update(kwargs)
    return profile
profile1 = build_user_profile(101, name="Анна", status="online", email="anna@example.com")
print(profile1)
profile2 = build_user_profile(202, first_name="Ашот", last_name="Арбузов", age=25, city="Москва")
print(profile2)
profile3 = build_user_profile(303)
print(profile3)