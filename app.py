from fastapi import Body, FastAPI, HTTPException
from bson import ObjectId
from bson.errors import InvalidId
from config.databaseconfig import clinic_collection
from Model.patientModel import PatientModel, PatientUpdateModel

app = FastAPI()


@app.get("/")   
async def home():
    return {"message": " Welcome to FastAPI. Congratulation you are connected to database...🚀"}


@app.get("/getPatient") 
async def get_patient():
    docs = await clinic_collection.find().to_list()
    for d in docs:
        d["_id"] = str(d["_id"])
    return docs

@app.post("/postPatient")
async def post_patient(data : PatientModel = Body(...)):
    docs = await clinic_collection.insert_one(data.model_dump())
    return {"message": "Patient added successfully", "id": str(docs.inserted_id)}

def _parse_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except InvalidId as exc:
        raise HTTPException(status_code=400, detail="Invalid patient id") from exc


@app.put("/updatePatient/{id}")
async def update_patient(id: str, data: PatientUpdateModel = Body(...)):
    object_id = _parse_object_id(id)
    update_doc = data.model_dump(exclude_unset=True, exclude_none=True)
    if not update_doc:
        raise HTTPException(status_code=400, detail="No fields provided to update")

    result = await clinic_collection.update_one({"_id": object_id}, {"$set": update_doc})
    if result.modified_count == 1:
        return {"message": "Patient updated successfully"}
    if result.matched_count == 1:
        return {"message": "No changes applied"}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.delete("/deletePatient/{id}")
async def delete_patient(id: str):
    object_id = _parse_object_id(id)
    result = await clinic_collection.delete_one({"_id": object_id})
    if result.deleted_count == 1:
        return {"message": "Patient deleted successfully"}
    raise HTTPException(status_code=404, detail="Patient not found")
