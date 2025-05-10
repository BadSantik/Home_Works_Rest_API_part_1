from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()


class Advertisement(BaseModel):
    id: int
    title: str
    description: str
    price: float
    author: str
    created_at: datetime


ads_db = [
    Advertisement(id=1, title="Apple iPhone 13", description="Latest Apple smartphone", price=699, author="Seller1", created_at=datetime.now()),
    Advertisement(id=2, title="Samsung Galaxy S21", description="Latest Samsung smartphone", price=799, author="Seller2", created_at=datetime.now()),
    Advertisement(id=3, title="Xiaomi Mi 11", description="High-quality Xiaomi smartphone", price=749, author="Seller3", created_at=datetime.now()),
    Advertisement(id=4, title="OnePlus 9 Pro", description="Premium OnePlus smartphone", price=969, author="Seller4", created_at=datetime.now()),
    Advertisement(id=5, title="Google Pixel 6", description="Cutting-edge Google smartphone", price=599, author="Seller5", created_at=datetime.now()),
    Advertisement(id=6, title="Nokia G50", description="Affordable Nokia smartphone", price=349, author="Seller6", created_at=datetime.now()),
    Advertisement(id=7, title="Sony Xperia 1 III", description="High-end Sony smartphone", price=1299, author="Seller7", created_at=datetime.now()),
    Advertisement(id=8, title="Huawei P40", description="Solid Huawei smartphone", price=499, author="Seller8", created_at=datetime.now()),
    Advertisement(id=9, title="Vivo X60 Pro", description="Innovative Vivo smartphone", price=599, author="Seller9", created_at=datetime.now()),
    Advertisement(id=10, title="Oppo Find X3 Pro", description="Stylish Oppo smartphone", price=1149, author="Seller10", created_at=datetime.now()),
]


@app.post("/advertisement", response_model=Advertisement)
def create_advertisement(ad: Advertisement):
    ads_db.append(ad)
    return ad


@app.patch("/advertisement/{advertisement_id}", response_model=Advertisement)
def update_advertisement(advertisement_id: int, ad: Advertisement):
    for index, existing_ad in enumerate(ads_db):
        if existing_ad.id == advertisement_id:
            ads_db[index] = ad
            return ad
    raise HTTPException(status_code=404, detail="Advertisement not found")


@app.delete("/advertisement/{advertisement_id}")
def delete_advertisement(advertisement_id: int):
    global ads_db
    ads_db = [ad for ad in ads_db if ad.id != advertisement_id]
    return {"detail": "Advertisement deleted"}


@app.get("/advertisement/{advertisement_id}", response_model=Advertisement)
def get_advertisement(advertisement_id: int):
    for ad in ads_db:
        if ad.id == advertisement_id:
            return ad
    raise HTTPException(status_code=404, detail="Advertisement not found")


@app.get("/advertisement", response_model=List[Advertisement])
def search_advertisement(title: str = None):
    if title:
        return [ad for ad in ads_db if title.lower() in ad.title.lower()]
    return ads_db