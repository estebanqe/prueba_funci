import reflex as rx

config = rx.Config(
    app_name="prueba_func",
    cors_allowed_origins=[
        "http://localhost:3000",
        "prueba-funci.vercel.app"
    ]
)