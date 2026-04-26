from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.config import get_db
from src.database.contacts.schemas import ContactCreateSchema, ContactUpdateSchema, ContactResponseSchema
from src.contacts.service import ContactService

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponseSchema])
async def read_contacts(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
):
    contact_service = ContactService(db)
    contacts = await contact_service.get_contacts(skip, limit, search)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponseSchema)
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contact = await contact_service.get_contact(contact_id)
    print(contact)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.post("/", response_model=ContactResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactCreateSchema, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    return await contact_service.create_contact(body)


@router.put("/{contact_id}", response_model=ContactResponseSchema)
async def update_contact(
    body: ContactUpdateSchema, contact_id: int, db: AsyncSession = Depends(get_db)
):
    contact_service = ContactService(db)
    contact = await contact_service.update_contact(contact_id, body)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.delete("/{contact_id}", response_model=ContactResponseSchema)
async def remove_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contact = await contact_service.remove_contact(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.get("/birthdays/upcoming", response_model=List[ContactResponseSchema])
async def upcoming_birthdays(db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    return await contact_service.get_upcoming_birthdays()
