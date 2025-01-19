from typing import Literal

from sqlalchemy import text


class PostgresHelper():
    @staticmethod
    def server_timezone(timezone: Literal["utc"] = "utc"):
        if timezone == "utc":
            return text("CURRENT_TIMESTAMP AT TIME ZONE 'UTC'")
        