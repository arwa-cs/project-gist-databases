import requests

def import_gists_to_database(db, username, commit=True):
    url = 'https://api.github.com/users/gvanrossum/gists'
    response = requests.get(url)
    gists = response.json()
    for gist in gists:
        gist_id = gist['id']
        github_id = gist['github_id']
        html_url = gist['html_url']
        git_pull_url = gist['git_pull_url']
        git_push_url = gist['git_push_url']
        commits_url = gist['commits_url']
        forks_url = gist['forks_url']
        public = gist['public']
        created_at = gist['created_at']
        updated_at = gist['updated_at']
        comments = gist['comments']
        comments_url = gist['comments_url']
        
        sql = """
            INSERT INTO gists (id, github_id,html_url, git_pull_url,git_push_url,commits_url,forks_url,public,created_at,updated_at,comments,comments_url)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """
        values = (gist_id,github_id,html_url,git_pull_url,git_push_url,commits_url,forks_url,public,created_at,updated_at,comments,comments_url)
        db.execute(sql,values)
        if commit:
            db.commit()
