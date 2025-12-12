from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session 
from app.schemas.post import PostOut, PostCreate 
from app.models.post import Post
from app.database.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/",response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(post_in: PostCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    #This route is protected: Only logged in users can post 
    new_post = Post(title = post_in.title, content = post_in.content, author_id = current_user.id)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/", response_model=List[PostOut])
def list_posts(db: Session = Depends(get_db)):
    # Public anyone can see posts 
    return db.query(Post).all()