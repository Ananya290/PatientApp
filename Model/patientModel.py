from typing import Annotated, Literal

from pydantic import BaseModel, Field, computed_field


class PatientAddress(BaseModel):
    pincode: Annotated[int, Field(..., description="Patient's pincode")]
    city: Annotated[str, Field(..., max_length=100, description="Patient's city")]
    state: Annotated[str, Field(..., max_length=100, description="Patient's state")]
    country: Annotated[str, Field(..., max_length=100, description="Patient's country")]


class PatientModel(BaseModel):
    id: Annotated[int, Field(..., description="Patient id")]
    name: Annotated[str, Field(..., max_length=100, description="Patient's name")]
    age: Annotated[int, Field(..., description="Patient's age")]
    city: Annotated[PatientAddress, Field(..., description="Patient's address")]
    gender: Annotated[
        Literal["Male", "Female", "Other"],
        Field(..., description="Patient's gender"),
    ]
    height: Annotated[float, Field(..., description="Patient's height in cm")]
    weight: Annotated[float, Field(..., description="Patient's weight in kg")]

    @computed_field
    def bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2

    @computed_field
    def health_status(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return "Underweight"
        if bmi < 24.9:
            return "Normal weight"
        if bmi < 29.9:
            return "Overweight"
        return "Obesity"


class PatientAddressUpdate(BaseModel):
    pincode: Annotated[int | None, Field(default=None, description="Patient's pincode")]
    city: Annotated[str | None, Field(default=None, max_length=100, description="Patient's city")]
    state: Annotated[str | None, Field(default=None, max_length=100, description="Patient's state")]
    country: Annotated[str | None, Field(default=None, max_length=100, description="Patient's country")]


class PatientUpdateModel(BaseModel):
    name: Annotated[str | None, Field(default=None, max_length=100, description="Patient's name")]
    age: Annotated[int | None, Field(default=None, description="Patient's age")]
    city: Annotated[PatientAddressUpdate | None, Field(default=None, description="Patient's address")]
    gender: Annotated[
        Literal["Male", "Female", "Other"] | None,
        Field(default=None, description="Patient's gender"),
    ]
    height: Annotated[float | None, Field(default=None, description="Patient's height in cm")]
    weight: Annotated[float | None, Field(default=None, description="Patient's weight in kg")]
