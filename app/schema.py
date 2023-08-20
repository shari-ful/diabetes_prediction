from pydantic import BaseModel


class PredictSchema(BaseModel):
    preg: int
    glucose: int
    bp: int
    st: int
    insulin: int
    bmi: float
    dpf: float
    age : int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "preg": 5,
                    "glucose": 120,
                    "bp": 92,
                    "st": 10,
                    "insulin": 81,
                    "bmi": 26.1,
                    "dpf": 0.551,
                    "age" : 67
                }
            ]
        }
    }
