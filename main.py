from fastapi import FastAPI
from problem import ProblemGenerator
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db.db_manager import DBManager

app = FastAPI()


app.add_middleware(                             
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

#data model for level post request body
class Input(BaseModel):
    level: str

#input model for save high score
class SaveScore(BaseModel):
    user_name: str
    level: str
    score: int

@app.get("/")
async def root():

    problem = ProblemGenerator.generate()
    
    return problem

@app.post("/")
async def difficulty(input: Input, status_code=200):

    problem = ProblemGenerator.generate_with_level(input.level)

    return problem

@app.post("/save_scores")
async def save_scores(input: SaveScore):

    manager = DBManager()
    saved_record = manager.save_score(user_name=input.user_name, level=input.level, score=input.score)

    #make this return the data saved
    return saved_record

@app.get("/get_scores")
async def get_scores():

    manager = DBManager()
    return manager.get_scores()
    


