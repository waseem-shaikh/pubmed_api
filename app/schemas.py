from pydantic import BaseModel, constr


class PublishDateModel(BaseModel):
    publication_date: constr(regex=r'^\d{4}-\d{2}-\d{2}$')
