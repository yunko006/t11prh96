from pydantic import BaseModel


class About(BaseModel):
    nom: str
    prenom: str
    age: int | None = None
    avatar: str | None = None
    role: str
    description: str | None = None


class AboutUpdate(BaseModel):
    nom: str | None = None
    prenom: str | None = None
    age: int | None = None
    avatar: str | None = None
    role: str | None = None
    description: str | None = None


# pas utiliser pour le moment
class AboutId(About):
    id: int
