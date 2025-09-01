import json
import sys
from database import orm
from entities.model import OwnerDTO

if "--init" in sys.argv:
    orm.Orm.init_db()
if "--insert" in sys.argv:
    orm.Orm.insert_test_data()



print("DATA owners")
owners = orm.Orm.get_owners_with_dogs()
result = OwnerDTO.model_validate(owners, from_attributes=True)
print(result)
