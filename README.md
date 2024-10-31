# TDSP1
A repo to be used for my Tools in Data Science Project of IITM
## How I scraped the data
1. **Setup and Imports**: The code imports necessary libraries like requests for API calls, CSV for data storage, and pandas for data processing. It uses ThreadPoolExecutor for multithreaded requests, speeding up data collection.

2. **API Token and Parameters**: User-configurable variables like GITHUB_TOKEN, CITY, and FOLLOWERS allow customization for the GitHub API queries, setting the authorization and search criteria.

3. **Header Configuration**: The GitHub API token is added to headers to authenticate requests, making it possible to access more data than unauthenticated requests allow.

4. **Data Collection with Multithreading**: ThreadPoolExecutor enables concurrent API requests, reducing total runtime. As threads complete, data is processed and stored, handling large volumes efficiently.

5. **Data Export**: Results are saved in a CSV format, ensuring data is easy to access, share, and analyze, with a final output file containing user details filtered by the city and follower count. 


## Interesting and Surprising Facts
1. There is no relation between the number of followers and the public repository.
2. Most of the developers are working in the Website Development domain while JavaScript is the most famous programming language.
3. People love to read the Markdown of a repository as it is the most starred one.
4. There is a slight increase in followers after each public repository is added.


## Actionable Recommendation for Developers
1. Focus on limited but quality projects. Number of projects you do is irrelevant.
2. You do need moderate popularity(around 250 followers) to be hireable in github.
3. Target ThoughtWorks, most of the developers in Chennai are working here. There is more chance of getting a job in that company.
4. Since 2020 Python has been the trending programming language. It will make you hireable if you learn Python.
