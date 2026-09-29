from datetime import datetime

from pydantic import BaseModel, Field


class SocialMediaPost(BaseModel):
    post_id: str
    platform: str
    user_id: str
    caption: str

    likes: int = Field(ge=0)
    comments: int = Field(ge=0)
    shares: int = Field(ge=0)
    reach: int = Field(ge=0)

    timestamp: datetime