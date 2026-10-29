from products_a import A
from products_b import B
from products_c import C
from products_d import D
from products_e import E
from products_f import F

REQUIRED = ["slug","display","folder","repo","firebase","replaces","wave","mission","platforms","money","why","port","screens","entities","ai","security_extra","m1","m2","m4","m6","risks"]
PRODUCTS = A + B + C + D + E + F
for p in PRODUCTS:
    missing = [k for k in REQUIRED if k not in p]
    assert not missing, (p.get("slug"), missing)
