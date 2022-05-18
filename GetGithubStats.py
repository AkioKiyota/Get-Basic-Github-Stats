from bs4 import BeautifulSoup
import requests


username = input("UserName: \n")

html = requests.get(f"https://github.com/{username}")

soup = BeautifulSoup(html.text, "lxml")

Repositories = soup.find('a', href="/AkioKiyota?tab=repositories")
Projects = soup.find("a", href="/AkioKiyota?tab=projects&type=beta")
Packages = soup.find("a", href="/AkioKiyota?tab=packages")
Stars = soup.find("a", href="/AkioKiyota?tab=stars")


Count_repositories = Repositories.find("span", class_="Counter")
Count_projects = Projects.find("span", class_="Counter")
Count_packages = Packages.find("span", class_="Counter")
Count_stars = Stars.find("span", class_="Counter")



print(f"Count of Repositories: {Count_repositories.text}, Count ofPorjects: {Count_projects.text}, " + 
      f"Count Of Packages: {Count_packages.text}, Count of Stars: {Count_stars.text}")

