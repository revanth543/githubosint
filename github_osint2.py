from github import Github
import time
import fnmatch
import re
 

# dorks.txt file is collected from https://github.com/techgaun/github-dorks 
def file_read():
	with open('dorks.txt') as file:
		content = file.readlines()
	content = [x.strip() for x in content]
	return content

list = file_read()
#print(list)


# Note: Gets rate limited and fails if too many hits


def extract_repo(dork):

# For using username and password
# g = Github("user", "password")

# Github Enterprise with custom hostname/domain
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# or using an access token

	g = Github('YOUR_API_KEY')
	repositories = set()
	content_files = g.search_code(query=dork)
	for content in content_files:
    		repositories.add(content.repository.full_name)
    		rate_limit = g.get_rate_limit()
    		if rate_limit.search.remaining == 0:
        		print('WARNING: Rate limit on searching was reached.  Results are incomplete.')
       			break
	rate_limit = g.get_rate_limit()
	print('Search results for the GITHUB dork:', dork)
	print(rate_limit.search)
	
	for repo in sorted(repositories):
			print(repo)
			directory = g.get_repo(repo)
			directory_contents = directory.get_contents("")
			while len(directory_contents) > 1:
				file_content = directory_contents.pop(0)
				if file_content.type == "dir":
					directory_contents.extend(directory.get_contents(file_content.path))	
				else:
					print(file_content)
					
for i in list:
	extract_repo(i)
	time.sleep(6)
	
'''

# Get Contents of a specific file manually
repo2 = g.get_repo("REPOSITORYNAME")
contents1 = repo2.get_contents("t/keys/1024_sign.pem")
raw_data = contents1.decoded_content
print(raw_data)


#extract the string
print(re.search('\"(.*)\"', str(file_content)))
					a = re.search('\"(.*)\"', file_content)
					directory_contents = directory.get_contents(a)
					raw_data = cdirectory_contents.decoded_content
					print(raw_data)
'''
