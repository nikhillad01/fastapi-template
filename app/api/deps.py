from app.database.db_session import SessionLocal


def get_connection():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    finally:
        db.close_all()
