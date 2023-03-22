import json
from pydantic import BaseModel

# class ShopeeItem(BaseModel):
#     itemid : str
#     shopid : int
#     name: str
#     currency : str
#     stock : int
#     sold: int
#     historical_sold: int
#     liked_count: int
#     brand: str
#     cmt_count: int
#     item_status: str
#     price: int
#     price_min: int
#     price_max: int
#     price_before_discount: int
#     show_discount: int
#     raw_discount: int
#     is_official_shop: bool
#     image: str
#     shop_location: str

with open("search_items.json", "r") as read_file:
    data = json.load(read_file)

js=[]

for i in data["items"]:
    jsdict={}
    fielddict={}
    ii = i["item_basic"]
    jsdict["model"] = "core.ShopeeItem"
    fielddict["itemid"] = ii["itemid"]
    fielddict["shopid"] = ii["shopid"]
    fielddict["name"] = ii["name"]
    fielddict["currency"] = ii["currency"]
    fielddict["stock"] = ii["stock"]
    fielddict["sold"] = ii["sold"]
    fielddict["historical_sold"] = ii["historical_sold"]
    fielddict["liked_count"] = ii["liked_count"]
    fielddict["brand"] = ii["brand"]
    fielddict["cmt_count"] = ii["cmt_count"]
    fielddict["item_status"] = ii["item_status"]
    fielddict["price"] = int(ii["price"]/100000)
    fielddict["price_min"] = int(ii["price_min"]/100000)
    fielddict["price_max"] = int(ii["price_max"]/100000)
    fielddict["price_before_discount"] = ii["price_before_discount"]
    fielddict["show_discount"] = ii["show_discount"]
    fielddict["raw_discount"] = ii["raw_discount"]
    fielddict["is_official_shop"] = ii["is_official_shop"]
    fielddict["image"] = ii["image"]
    fielddict["shop_location"] = ii["shop_location"]
    jsdict["fields"] = fielddict.copy()
    js.append(jsdict.copy())

# print(js[0]["fields"]["price"])
with open("shopeeitems.json","w") as w:
    json.dump(js,w,indent=4)