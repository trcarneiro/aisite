from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas, database
from app.auth import get_current_user

router = APIRouter(tags=["projects"])

@router.post("/", response_model=schemas.Project)
async def create_project(
    project: schemas.ProjectCreate, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    return await crud.create_project(db, project)

@router.get("/", response_model=list[schemas.Project])
async def read_projects(
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    return await crud.get_projects(db)

@router.get("/{project_id}", response_model=schemas.Project)
async def read_project(
    project_id: int, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_project = await crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.put("/{project_id}", response_model=schemas.Project)
async def update_project(
    project_id: int, 
    project: schemas.ProjectUpdate, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_project = await crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return await crud.update_project(db, db_project, project)

@router.delete("/{project_id}", response_model=schemas.Project)
async def delete_project(
    project_id: int, 
    db: AsyncSession = Depends(database.get_db), 
    current_user: schemas.User = Depends(get_current_user)
):
    db_project = await crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    await crud.delete_project(db, db_project)
    return db_project
