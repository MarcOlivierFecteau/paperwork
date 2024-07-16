from paperwork import db
from flask_login import UserMixin
import typing
from pydantic import BaseModel


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    cip = db.Column(db.String(8), unique=True)
    password = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    tel = db.Column(db.String(12))


class Group(BaseModel):
    _type: str
    name: str


class Contact(BaseModel):
    name: str
    email: str
    tel: typing.Optional[str] = None


class ReimbursementForm(BaseModel):
    group: Group
    contact: Contact
    supplier: bool
    payment_entity_name: str
    purchase_amount: float
    currency: str
    purchase_amount_cad: typing.Optional[float] = None
    payment_method: str
    physical_proof: bool
    financing_activity: bool
    for_profit: bool
    activity_name: typing.Optional[str] = None
    purchase_description: typing.Optional[str] = None
    purchase_date: str


class KmForm(BaseModel):
    group: Group
    contact: Contact
    applicant_name: str
    start_addr: str
    dest_addr: str
    trip_dist: float
    rate: float
    amount: float
    payment_method: str
    financing_activity: bool
    for_profit: bool
    trip_date: str
    trip_reason: typing.Optional[str] = None
