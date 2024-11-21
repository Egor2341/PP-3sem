import enum


class Status(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"