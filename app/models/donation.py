from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base import BaseTable


class Donation(BaseTable):
    user_id = Column(
        Integer, ForeignKey("user.id", name="fk_reservation_user_id_user")
    )
    comment = Column(Text)
