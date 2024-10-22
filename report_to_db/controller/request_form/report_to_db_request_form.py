from pydantic import BaseModel

from report_to_db.service.request.report_to_db_request import ReportToDbRequest


class ReportToDbRequestForm(BaseModel):
    userToken: str

    def toAiReportToDbRequest(self) -> ReportToDbRequest:
        return ReportToDbRequest(userToken=self.userToken)