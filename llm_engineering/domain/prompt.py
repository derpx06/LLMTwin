from .base import VectorBaseDocument
from .cleaned_documents import CleanedDocument
from .types import DataCategory

class Prompt(VectorBaseDocument):
    template:str
    input_variables:str
    content:str
    num_tokens:int|None = None

    class Config:
        category = DataCategory.PROMPT

class GenerateDatasetSamplesPrompt(Prompt):
    data_category:DataCategory
    document:CleanedDocument
