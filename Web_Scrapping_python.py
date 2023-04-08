from bs4 import BeautifulSoup
import time

print('Put some skills that you are not familiar with')
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}')

# 1) if we have that website '.html' file

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     # print(content)

#     # soup = BeautifulSoup(content, 'lxml')
#     # print(soup.prettify)

#     # tags = soup.find('h5')  
#     # print(tags)  --> display only 1st h5 tag

#     # courses_html_tags = soup.find_all('h5')
#     # print(courses_html_tags)  --> display all h5 tags
#     # for courses in courses_html_tags:
#     #     print(courses.text)

#     soup = BeautifulSoup(content, 'lxml')
#     course_cards = soup.find_all('div', class_='card')

#     for course in course_cards:
#         # print(course.h5)  --> display 3 courses
#         course_name = course.h5.text
#         course_price = course.a.text
#         print(course_price)
#         course_price = course.a.text.split()[-1]

#         print(course_price)

## ---------------------------------------------------------------------------------------------------------- ##

# 2) we don't have website '.html' file, so we use 'requests' library to access url

import requests


def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Machine+Learning%2CSoftware+Engineer&txtLocation=Gujarat&cboWorkExp1=2"

    html_text = requests.get(url).text
    # print(html_text)

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):

        # Extra 
        # --> if you want to show only some particular published date output 
        published_date = job.find('span', class_="sim-posted").text
        if 'few' in published_date:

            company_name = job.find('h3', class_="joblist-comp-name").text
            # company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ','')
            # print(company_name)

            skills = job.find('span', class_="srp-skills").text.replace(' ,', ',')
            # print(skills) 

            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")

                print(f'File saved: {index}')

                # print(f"Company Name: {company_name.strip()}\n")
                # print(f"Required Skills: {skills.strip()}\n")
                # print(f"More Info: {more_info}\n")
                # comment out above because we also want to save the data in another file
                # hence we use file I/O methods in above lines 


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes..')
        time.sleep(time_wait * 60)
