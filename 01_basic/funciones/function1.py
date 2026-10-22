# Codigo facilito

# kwargs
# **(nombres) -> Dictionary 


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")

show_info(
    username="Cody",
    email="cody@codigofacilito.com",
    password="1234",
    active=True,
    courses=["Python", "Django", "FastAPI"],
    last_login="2025",
    is_super_user=True
)