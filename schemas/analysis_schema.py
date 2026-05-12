from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Dict
class analysis_schema(BaseModel):
    company_overview:     Dict
    recent_news_summary:  List[Dict]
    sentiment:            str
    risks:                Optional[Dict]
    opportunities:        Optional[Dict]
    investment_thesis:    Optional[Dict]
