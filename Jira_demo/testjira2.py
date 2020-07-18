from jira import JIRA
from pprint import pprint

project_name="Cloud - Workstreams"
jiraURL="https://myjira.test.com"
username="anikm1987"
password="password"

jira = JIRA(jiraURL,auth=(username, password))


print("Summaries of my last 3 reported issues :")
# Summaries of my last 3 reported issues  - in place of anikm1987 use currentUser() for default
for issue in jira.search_issues('reporter = nk342761 order by created desc', maxResults=1):
    print(issue)
