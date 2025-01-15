from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from ..database.db_config import Base

class Role(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)    


class User(Base):
    __tablename__ = "users"
        
    username = Column(String(100), primary_key=True, unique=True, index=True)    
    password = Column(String(100), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

class Product_Service(Base):
    __tablename__ = "products_services"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)  

class Channel(Base):
    __tablename__ = "Channels"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)  

class Risk_Category(Base):
    __tablename__ = "Risk_Categories"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)  
  
class Risk_Type(Base):
    __tablename__ = "Risk_Types"

    id = Column(Integer, primary_key=True, index=True)
    Category_id = Column(Integer, ForeignKey('Risk_Categories.id'), nullable=False)
    description = Column(String(255), nullable=False) 

class Macroprocess(Base):
    __tablename__ = "Macroprocesses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False) 

class Process(Base):
    __tablename__ = "Processes"

    id = Column(Integer, primary_key=True, index=True)
    macroprocess_id = Column(Integer, ForeignKey('Macroprocesses.id'), nullable=False)
    description = Column(String(255), nullable=False) 

class Risk_Factor(Base):
    __tablename__ = "Risk_Factors"

    id = Column(Integer, primary_key=True, index=True)
    risk_type_id = Column(Integer, ForeignKey('Risk_Types.id'), nullable=False)  # Clave foránea
    description = Column(String(255), nullable=False)

class Impact(Base):
    __tablename__ = 'Impact' 

    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, nullable=False) 
    description = Column(String(255), nullable=False) 
    definition = Column(Text)  
    criteria_smlv = Column(Numeric(10, 2))

class Probability(Base):
    __tablename__ = 'Probability' 

    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, nullable=False) 
    description = Column(String(255), nullable=False) 
    definition = Column(Text)  
    criteria_smlv = Column(Numeric(5, 2))

class Risk_Control_Types(Base):
    __tablename__ = "Risk_Control_Types"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False) 

class Control(Base):
    __tablename__ = 'controls'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    control_type_id = Column(Integer, ForeignKey('risk_control_types.id'), nullable=False)  
    description = Column(String(255), nullable=False)
    frequency = Column(String(100), nullable=True)  
    responsible_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    risk_type_id = Column(Integer, ForeignKey('risk_types.id'), nullable=False)  
    factor = Column(String(255), nullable=True)  
    description = Column(Text, nullable=False)  
    probability_id = Column(Integer, ForeignKey('probability.id'), nullable=False)
    impact_id = Column(Integer, ForeignKey('impact.id'), nullable=False)


class Event_Log(Base):
    __tablename__ = 'event_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    event_code = Column(String(50), nullable=True) 
    start_date = Column(DateTime, nullable=False) 
    end_date = Column(DateTime, nullable=True)
    discovery_date = Column(DateTime, nullable=True)  
    accounting_date = Column(DateTime, nullable=True) 
    amount = Column(Numeric(10, 2), nullable=True) 
    recovered_amount = Column(Numeric(10, 2), nullable=True) 
    insurance_recovery = Column(Numeric(10, 2), nullable=True) 
    risk_factor_id = Column(Integer, ForeignKey('risk_factors.id'), nullable=True) 
    product_id = Column(Integer, ForeignKey('products_services.id'), nullable=True) 
    process_id = Column(Integer, ForeignKey('processes.id'), nullable=True)
    channel_id = Column(Integer, ForeignKey('channels.id'), nullable=True) 
    city = Column(String(100), nullable=True) 
    responsible_id = Column(Integer, ForeignKey('users.id'), nullable=True)  
    status = Column(String(50), nullable=True) 

class Cause(Base):
    __tablename__ = 'causes'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    description = Column(String(255), nullable=False) 
    risk_factor_id = Column(Integer, ForeignKey('risk_factors.id'), nullable=False)  
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False) 

class Personal(Base):
    __tablename__ = 'personal'

    id = Column(Integer, primary_key=True, autoincrement=True)  
    name = Column(String(100), nullable=False) 
    position = Column(String(100), nullable=False) 
    area = Column(String(100), nullable=True) 
    process_id = Column(Integer, ForeignKey('processes.id'), nullable=True)  
    email = Column(String(255), nullable=True)   

class Tracking(Base):
    __tablename__ = 'tracking'

    id = Column(Integer, primary_key=True, autoincrement=True) 
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  
    control_id = Column(Integer, ForeignKey('controls.id'), nullable=False)  
    event_id = Column(Integer, ForeignKey('event_logs.id'), nullable=False)  
    tracking_date = Column(DateTime, nullable=False) 