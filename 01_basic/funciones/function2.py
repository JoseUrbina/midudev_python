# *(posición) - tuple
# **(nombre) - dictionary

def show_info(*args, **kwargs):
    print(">>> Info")
    for value in args:
        print(value)

    print("\n>>> Details")
    for key, value in kwargs.items():
        print(f"{key} - {value}")

show_info(
    "Cody", "Facilito", 12, "cody@codigofacilito.com",
    courses=["Python", "Flask", "Django"],
    score=10,
    active=True,
    is_super_admin=True        
)
