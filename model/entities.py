from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Usuario(connector.Manager.Base):
    __tablename__ = 'alumno'
    alumno_id = Column(Integer, Sequence('Usuario'), primary_key=True)
    nombre = Column(String(50))
    ciclo = Column(String(12))
    carrera = Column(Integer)