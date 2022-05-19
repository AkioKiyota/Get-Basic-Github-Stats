from bs4 import BeautifulSoup
import requests

username = input("UserName: \n")

html = requests.get(f"https://github.com/{username}")
soup = BeautifulSoup(html.text, "lxml")

repositories = soup.find('a', href=f"/{username}?tab=repositories")
projects = soup.find("a", href=f"/{username}?tab=projects&type=beta")
packages = soup.find("a", href=f"/{username}?tab=packages")
stars = soup.find("a", href=f"/{username}?tab=stars")

count_repositories = Repositories.find("span", class_="Counter")
count_projects = Projects.find("span", class_="Counter")
count_packages = Packages.find("span", class_="Counter")
count_stars = Stars.find("span", class_="Counter")

print(f"Number of repositories: {count_repositories.text}, Number of projects: {count_projects.text}, " + 
      f"Number of Packages: {count_packages.text}, Number of Stars: {count_stars.text}")
