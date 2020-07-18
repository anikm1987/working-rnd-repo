from jira import JIRA
from pprint import pprint

project_name="Cloud - Workstreams"
jiraURL="https://myjira.test.com"
username="anikm1987"
password="password"

jira = JIRA(jiraURL,auth=(username, password))

# Get an issue.
issue = jira.issue("CW-814")
pprint(issue)

print("Summaries of my last 3 reported issues :")
# Summaries of my last 3 reported issues  - in place of anikm1987 use currentUser() for default AND status IN ("To Do", "In Progress")
for issue in jira.search_issues('reporter = nk342761 order by created desc', maxResults=3):
    print('{}: {}'.format(issue.key, issue.fields.summary))



print("my top 5 issues due by the end of the week :")
# my top 5 issues due by the end of the week, ordered by priority and due < endOfWeek() 
oh_crap = jira.search_issues('assignee = currentUser() order by priority desc', maxResults=5)
for issue in oh_crap:
  print('{}: {}'.format(issue.key, issue.fields.summary))

print("All project Issues but not assigned to me :")
# Search returns first 50 results, `maxResults` must be set to exceed this
#issues_in_proj = jira.search_issues('project=PROJ')
all_proj_issues_but_mine = jira.search_issues('project="{0}" and assignee != currentUser()'.format(project_name))
for issue in all_proj_issues_but_mine:
  print('{}: {}'.format(issue.key, issue.fields.summary))



