# *(posición) - tuple
# **(nombre) - dictionary

"""
    Función con diferentes tipos de parametros

    1. obligatorios
    2. *args
    3. opcionales
    4. **kwargs
"""
def show_info(username, last_name, *args, active=True, is_super_admin=False, **kwargs):
    print(f"Username: {username}")
    print(f"Last name: {last_name}")

    print("\n>>> Extra info")
    for value in args:
        print(value)

    print(f"Active: {active}")
    print(f"Super Admin: {is_super_admin}")

    print("\n>>> Details")
    for key, value in kwargs.items():
        print(f"{key} - {value}")

show_info(
    "Cody", "Facilito",
    "info@codigofacilito.com", "password123", # args
    active=False, is_super_admin=True,
    courses=["Python", "FastAPI"], is_deleted=False # kwargs
)
