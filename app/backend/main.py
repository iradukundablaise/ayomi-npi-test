from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from io import StringIO
import csv

from app.models import Result
from app.database import session, engine

from app.utils.npi_calculator import NpiCalculator

app = FastAPI()

SQLModel.metadata.create_all(engine)

# cors middleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate", summary="Evaluer une expression en notation polonaise inversée", description="Cette route permet d'évaluer une expression en notation polonaise inversée")
async def calculate_npi(expr: str):
    """
    This function evaluates an expression in reverse polish notation
    :param expr: expression to evaluate in string format
    :return: evaluation result
    """
    npi = NpiCalculator(expr)
    try:
        evaluationResult = npi.evaluate()

        # save results into the database
        result = Result(express=expr, results=evaluationResult)

        session.add(result)
        session.commit()

        return { "expression": expr, "results": evaluationResult }

    except Exception as e:
        return { "error": "npi syntax is incorrect" }


@app.get("/export-csv", summary="Exporter les données en CSV", description="Cette route permet d'exporter les données de la base de données en format CSV")
async def export_data():
    """
    This function exports NPI results data from the database into a CSV file
    :return: Response CSV file
    """

    # fetch all results from the database
    query = session.query(Result)
    results = query.all()

    if len(results) > 0:
        output = StringIO()
        writer = csv.writer(output)

        # write the header
        writer.writerow(["id", "expression", "results"])

        # write the data
        for result in results:
            writer.writerow([result.id, result.express, result.results])

        output.seek(0)

        response = Response(content=output.getvalue(), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=results.csv"

        return response
    else:
        return { "message": "No data to export" }