import sys
sys.path.append('database')
from database.database import get_db, insert_test, find_by_test_id
from io import BytesIO
import json
import uuid


db = get_db()

test_id = uuid.uuid4()
description = "short-term memory test"
patient_id = uuid.uuid4()

insert_test(db, test_id, description, patient_id, 100)

results = find_by_test_id(db, test_id)
for result in results:
    print(result['test_score'])