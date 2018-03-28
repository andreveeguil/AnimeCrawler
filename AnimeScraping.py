from selenium import webdriver

# list_keywords = ['Sugawara', 'Takase', 'Kanda', 'Furuya', 'Minagawa', 'Ayane']
# list_keywords = ['Chiaki', 'Uchimura', 'Kana', 'Iijima', 'Takeru', 'Gouda', 'Ayaka', 'Kaji', 'Akagi', 'LoveMaster', 'Love Master', 'Kazuko', 'Hosokawa']

list_keywords = ['Kamine', 'Ryouko']

path_to_chromedriver = '/Users/ahartanto/Code/chromedriver'
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://mangarock.com/manga/mrs-serie-100187117'
browser.get(url)

for keyword in list_keywords:
	print("List for " + keyword)
	xpath_match = '//a[contains(text(), "{}")]'.format(keyword)
	result = browser.find_elements_by_xpath(xpath_match)

	chapter_list = []
	for match in result:
		chapter = match.text.split(' ')[2].strip(':')
		chapter_list.append(int(chapter))

	chapter_list.sort()
	for chapter in chapter_list:
		print("*[[Chapter " + str(chapter) + ']]')
