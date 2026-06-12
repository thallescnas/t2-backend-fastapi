from fastapi import APIRouter, Depends, HTTPException
from database import get_db, engine
from schemas.CarSchemas import CarRegister, CarUpdate, CarResponse
from models.Car import Car, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/cars")

@router.get("/", response_model=list[CarResponse])
def allCars(db: Session = Depends(get_db)):
    return db.query(Car).all()

@router.get("/{car_id}", response_model=CarResponse)
def get_Car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()

    if not car:
        raise HTTPException(404, "Car not found!")
    
    return car

@router.post("/", response_model=CarResponse)
def create_car(car: CarRegister ,db: Session = Depends(get_db)):
    cr = Car(**car.model_dump())
    db.add(cr)
    db.commit()
    db.refresh(cr)
    return cr

@router.delete("/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    cr = db.query(Car).filter(Car.id == car_id).first()

    if not cr:
        raise HTTPException(404, "Car not found!")
    
    db.delete(cr)
    db.commit()
    
    return {"message": "Carro deletado com sucesso!"}

@router.patch("/{car_id}", response_model=CarResponse)
def update_car(car_id: int, up: CarUpdate ,db: Session = Depends(get_db)):
    cr = db.query(Car).filter(Car.id == car_id).first()

    if not cr:
        raise HTTPException(404, "Car not found!")
    
    upd = up.model_dump(exclude_unset=True)

    for key, value in upd.items():
         setattr(cr, key, value)

    db.commit()
    db.refresh(cr)
    
    return cr


@router.get("/latest", response_model=CarResponse)
def get_latest_car(db: Session = Depends(get_db)):
    cr = db.query(Car).order_by(Car.id.desc()).first()

    if not cr:
        raise HTTPException(404, "Car not found!")
    
    return cr

