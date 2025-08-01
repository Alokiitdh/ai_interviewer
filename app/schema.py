from pydantic import BaseModel, field_validator

# Question Agent output
class QuestionResponse(BaseModel):
    topic: str
    question: str
    

# Evaluation Agent output
class EvaluationResponse(BaseModel):
    question:str
    user_answer: str
    score: int  # out of 10
    evaluation_summary: str # max 250 chars
    
    @field_validator("score", mode="before")
    def convert_score(cls, v):
        return int(v)


# Performance Agent output
class PerformanceResponse(BaseModel):
    final_score: int  # out of 100
    performance_summary: str  # 250 characters or less
