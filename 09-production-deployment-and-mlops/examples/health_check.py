def health_check() -> dict:
    return {"status": "healthy", "version": "1.0.0"}


print(health_check())
