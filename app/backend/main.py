from app.utils.npi_calculator import NpiCalculator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# cors middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/evaluate")
async def calculate_npi(expr: str):
    npi = NpiCalculator(expr)
    try:
        result = npi.evaluate()
        return { "expression": expr, "results": result }

    except Exception as e:
        return { "error": "npi syntax is incorrect" }


@app.get("/export-csv")
async def export_data():
    return { "message": "exporting data"}