from fastapi import APIRouter, HTTPException

from app.schemas.project import Project, ProjectCreate, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["projects"])

projects_db: dict[int, Project] = {}
_next_id: int = 1


@router.get("", response_model=list[Project])
async def get_all_projects() -> list[Project]:
    return list(projects_db.values())


@router.get("/{project_id}", response_model=Project)
async def get_project(project_id: int) -> Project:
    project = projects_db.get(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("", response_model=Project, status_code=201)
async def create_project(payload: ProjectCreate) -> Project:
    global _next_id
    project = Project(id=_next_id, **payload.model_dump())
    projects_db[_next_id] = project
    _next_id += 1
    return project


@router.put("/{project_id}", response_model=Project)
async def update_project(project_id: int, payload: ProjectUpdate) -> Project:
    project = projects_db.get(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    updated = project.model_copy(update={k: v for k, v in payload.model_dump().items() if v is not None})
    projects_db[project_id] = updated
    return updated


@router.delete("/{project_id}", status_code=204)
async def delete_project(project_id: int) -> None:
    if project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Project not found")
    del projects_db[project_id]
