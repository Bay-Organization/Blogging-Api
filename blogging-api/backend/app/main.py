from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine, Base
from app.models import user, post, comment, like
from app.routes import users, posts, comments, likes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blogging API",
    version="0.1.0",
)

# ✅ CORS: allow your React frontend to call this API
# Vite dev server is usually: http://localhost:5173
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # If you deploy frontend later, add your domain here:
    # "https://your-frontend-domain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # or ["*"] for quick testing (NOT recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],            # allows Authorization header
)

# ✅ Routers
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(likes.router)

# Optional: quick test endpoint
@app.get("/")
def root():
    return {"message": "Blogging API is running"}
