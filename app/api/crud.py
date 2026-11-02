from typing import Any
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

def list_items(db: Session, model: Any, skip: int, limit: int):
    return list(db.scalars(select(model).offset(skip).limit(limit)).all())

def get_item(db: Session, model: Any, item_id: int):
    item = db.get(model, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro no encontrado")
    return item

def create_item(db: Session, model: Any, data: Any):
    item = model(**data.model_dump())
    db.add(item)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=409, detail="La operación viola una relación o restricción única") from exc
    db.refresh(item)
    return item

def update_item(db: Session, model: Any, item_id: int, data: Any):
    item = get_item(db, model, item_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    return create_or_commit(db, item)

def create_or_commit(db: Session, item: Any):
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=409, detail="La operación viola una relación o restricción única") from exc
    db.refresh(item)
    return item

def delete_item(db: Session, model: Any, item_id: int):
    item = get_item(db, model, item_id)
    db.delete(item)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=409, detail="No se puede eliminar porque el registro está relacionado") from exc
    return {"message": "Registro eliminado", "id": item_id}
