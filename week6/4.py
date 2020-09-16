import bs4
import requests
response = requests.get('https://www.borntodev.com/blog/')
page_data = bs4.BeautifulSoup(response.text,'html.parser')
data_list = page_data.find_all("div",class_="post-header")
for i in data_list:
    st =str(i)
    post = st.find('"https')
    newst = st[post::]
    newa =" "
    for a in newst:
        if a != ">":
            newa = newa+a
        else:
            break
    print(i.text,"| link:",newa)
    print("-------------------")