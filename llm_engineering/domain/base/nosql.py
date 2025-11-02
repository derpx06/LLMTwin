import uuid
from abc import ABC
from typing import Generic, Type, TypeVar

from loguru import logger
from pydantic import UUID4, BaseModel, Field
from pymongo import errors

from ..exceptions import ImproperlyConfigured
from llm_engineering.infrastructure.db.mongo import Mongo