"""
Announcements endpoints for the High School Management System API
"""

from fastapi import APIRouter
from typing import List, Dict, Any

from ..database import announcements_collection

router = APIRouter(
    prefix="/announcements",
    tags=["announcements"]
)


@router.get("", response_model=List[Dict[str, Any]])
@router.get("/", response_model=List[Dict[str, Any]])
def get_announcements() -> List[Dict[str, Any]]:
    """
    Get all active announcements ordered by priority
    """
    # Query for active announcements and sort by priority
    announcements = []
    for announcement in announcements_collection.find({"active": True}).sort("priority", 1):
        # Remove MongoDB _id field for cleaner JSON response
        announcement.pop('_id', None)
        announcements.append(announcement)
    
    return announcements
