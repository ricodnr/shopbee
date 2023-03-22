import json
from pydantic import BaseModel

class ShopeeItem(BaseModel):
    itemid : str
    shopid : int
    name: str
    currency : str
    stock : int
    sold: int
    historical_sold: int
    liked_count: int
    brand: str
    cmt_count: int
    item_status: str
    price: int
    price_min: int
    price_max: int
    price_before_discount: int
    show_discount: int
    raw_discount: int
    is_official_shop: bool
    image: str
    shop_location: str

with open("search_items.json", "r") as read_file:
    data = json.load(read_file)

js=[]

for i in data["items"]:
    jsdict={}
    ii = i["item_basic"]
    
    item_ins = ShopeeItem(
        **ii,
        price = ii["price"]/10000,
        )
    jsdict["model"] = "core.ShopeeItem"
    jsdict["fields"] = item_ins.dict()
    js.append(jsdict.copy())

with open("shopeeitems.json","w") as w:
    json.dump(js,w,indent=2)