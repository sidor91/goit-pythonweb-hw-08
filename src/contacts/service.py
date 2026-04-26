from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from fastapi import HTTPException, status

from src.contacts.repository import ContactRepository
from src.database.contacts.schemas import ContactCreateSchema, ContactUpdateSchema
from src.utils.error_handlers import handle_integrity_error

class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def create_contact(self, body: ContactCreateSchema):
        try:
            return await self.repository.create_contact(body)
        except IntegrityError as e:
            message = handle_integrity_error(e)
            raise HTTPException(400, detail=message)
        except SQLAlchemyError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error",
            )

    async def get_contacts(self, skip: int, limit: int, search: str | None = None):
        try:
            return await self.repository.get_contacts(skip, limit, search)
        except SQLAlchemyError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error",
            )

    async def get_contact(self, contact_id: int):
        try:
            contact = await self.repository.get_contact_by_id(contact_id)
            return contact
        except SQLAlchemyError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error",
            )

    async def update_contact(self, contact_id: int, body: ContactUpdateSchema):
        try:
            contact = await self.repository.update_contact(contact_id, body)
            return contact
        except IntegrityError as e:
            message = handle_integrity_error(e)
            raise HTTPException(400, detail=message)
        except SQLAlchemyError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error",
            )

    async def remove_contact(self, contact_id: int):
        try:
            contact = await self.repository.remove_contact(contact_id)
            return contact
        except SQLAlchemyError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error",
            )


    async def get_upcoming_birthdays(self):
        try:
            return await self.repository.get_upcoming_birthdays()
        except SQLAlchemyError:
            raise HTTPException(500, "Database error")