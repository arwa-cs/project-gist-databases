from .models import Gist

def search_gists(db_connection, **kwargs):
    query = "SELECT * FROM gists"
    params = {}

    if github_id:
        query += " WHERE github_id = :github_id"
        params["github_id"] = github_id

    if created_at:
        if github_id:
            query += " AND"
        else:
            query += " WHERE"
        query += " datetime(created_at) = datetime(:created_at)"
        params["created_at"] = created_at

    cursor = db_connection.execute(query, params)
    results = cursor.fetchall()

    gists = []
    for result in results:
        gists.append(Gist(*result))

    return gists
