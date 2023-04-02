from app.core.db import AsyncSessionLocal
from app.models.meeting_room import MeetingRoom
from app.schemas.meeting_room import MeetingRoomCreate


async def create_meeting_room(new_room: MeetingRoomCreate) -> MeetingRoom:
    new_room_data =new_room.dict()
    db_room = MeetingRoom(**new_room_data) #Двойная звездочка (**) в Python используется для распаковки словаря.
    #В данном случае, new_room_data является словарем, содержащим данные для создания новой комнаты.
    # Использование ** перед словарем позволяет передать его содержимое как именованные аргументы в конструктор класса MeetingRoom.

    # Создаём асинхронную сессию через контекстный менеджер.
    async with AsyncSessionLocal() as session:
        session.add(db_room)
        await session.commit()
        # Обновляем объект db_room: считываем данные из БД, чтобы получить его id.
        await session.refresh(db_room)
    # Возвращаем только что созданный объект класса MeetingRoom.
    return db_room
