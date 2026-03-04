import sqlite3
from crewai.tools import BaseTool


class SQLTool(BaseTool):
    name: str = "Database Query Tool"
    description: str = """
    Useful for querying structured applicant data.
    Input must be a valid SQL SELECT query.
    """

    def _run(self, query: str) -> str:
        conn = sqlite3.connect("data/company.db")
        cursor = conn.cursor()

        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except Exception as e:
            results = f"SQL Error: {e}"

        conn.close()
        return str(results)