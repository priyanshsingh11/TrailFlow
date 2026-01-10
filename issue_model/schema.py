from dataclasses import dataclass
from datetime import datetime


@dataclass
class Issue:
    issue_id: str
    study_id: str
    domain: str
    issue_type: str
    severity: str
    description: str
    entity_id: str | None
    source_file: str
    detected_at: datetime
