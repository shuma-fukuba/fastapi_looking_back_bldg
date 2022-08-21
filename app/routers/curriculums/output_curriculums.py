from fastapi import APIRouter
from sqlalchemy.orm import Session
from database import get_db

from models import InputCurriculum, User
from cruds.curriculums import input_curriculums as crud


router = APIRouter()
