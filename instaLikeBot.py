from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

	
uname = 'XXXXXX'
upswd = 'XXXX'	

def login(uname,upswd,browser):
	uname_field = browser.find_element_by_name("username")
	uname_field.send_keys(uname)

	upswd_field = browser.find_element_by_name("password")
	upswd_field.send_keys(upswd + Keys.RETURN)
	time.sleep(5)

def surf_instagram():
	browser = webdriver.Chrome()
	browser.get("https://www.instagram.com")
	time.sleep(3)	

	return browser

def reach_homepage(browser):
	
	pswd_notnow = browser.find_element_by_xpath('/html/body/div/section/main/div/div/div/div/button')
	pswd_notnow.click()

	time.sleep(2)
		
	notfc_notnow = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
	notfc_notnow.click()

	time.sleep(1)

def fpost_like(browser):
	post_likebtn = browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div/div[2]/div/article/div[2]/section[1]/span[1]/button')
	post_likebtn.click()

def search_hashtag(hashtag,browser):
	search_bar = browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
	search_bar.send_keys(f'#{hashtag}')
	time.sleep(2)
	
	search_bar.send_keys(Keys.RETURN)
	search_bar.send_keys(Keys.RETURN)
	search_bar.send_keys(Keys.RETURN)


def open_fphoto(browser):
	top = "_9AhH0"
	top_post = browser.find_element_by_class_name(top)
	top_post.click()

def like_and_next(browser):
	# like_button = browser.find_element_by_class_name("_8-yf5")
	like_button = browser.find_element_by_xpath("html/body/div[3]/div[2]/div/article/div[3]/section[1]/span[1]/button")
	like_button.click()
	# like_button.click()
				
	body_elem = browser.find_element_by_xpath('/html/body')
	body_elem.send_keys(Keys.RIGHT)

def comment_and_next(browser):
	time.sleep(2)
	comment_field = browser.find_element_by_xpath('html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
	# comment_field = browser.find_element_by_class_name('Ypffh')
	time.sleep(5)
	comment_field.send_keys('nice composition!!')
	# time.sleep(1)
	comment_field.send_keys(Keys.RETURN)

	time.sleep(2)
	body_elem = browser.find_element_by_xpath('/html/body')
	body_elem.send_keys(Keys.RIGHT)

def read_file():

	hash_list = []
	read_file = open("myFile.txt",'r')
	for line in read_file:
		hash_list.append(line[:-1])
	
	read_file.close()
	return hash_list
	
def write_file(new_hashlist):
	
	file = open("myFile.txt",'w')
	for val in new_hashlist:
		file.write(f'{val}\n')
	
	file.close()

def collect_hashtag(search_keywrds,hash_num,browser):
	new_tags = []
	for hashtag in search_keywrds:
		# searching for hashtag in search bar
		time.sleep(1)
		search_hashtag(hashtag,browser)
		time.sleep(5)
		div_count = int(hash_num)
		
		for num in range(div_count):
			hashpath_string = str(num+1)
			hashpath = f'html/body/div[1]/section/main/header/div[2]/div[2]/span/span[2]/div[{hashpath_string}]/a'
			try:
				time.sleep(1)
				my_hashtag = browser.find_element_by_xpath(hashpath).text
				new_tags.append(my_hashtag[1:])
			except:
				print(f'No hashtag found. at {hashtag}')
				pass
		
		
	write_file(new_tags)


total_likes = 0
total_comment = 0	

browser = surf_instagram()

login(uname,upswd,browser)

reach_homepage(browser)

# collect_hashtag(['earthpix','natgeo'],'2',browser)

# hashtag_list = read_file()
hashtag_list = ['natgeotravel','wanderlust','moscow']

# choosing hashtag from hashtag list
for hashtag in hashtag_list:
		
	# searching for hashtag in search bar
	time.sleep(3)
	search_hashtag(hashtag,browser)

	# opening first most recent picture
	time.sleep(3)
	try:
		open_fphoto(browser)
	except:
		time.sleep(5)
		open_fphoto(browser)

	# like count for choosen hashtag from hashtag list
	count = 0
	
	# like picture and go to next
	for x in range(1,101):	
		time.sleep(1)
		# try:
		like_and_next(browser)
		count += 1
		# except:
			# print(f'Error took place at : {count} iteration, with hashtag : {hashtag}')
			# time.sleep(2)
			# break			


	total_likes += count

	# comment on picture and go to next
	# for x in range(1,5):	
	# 	time.sleep(1)
	# 	comment_and_next(browser)
		# count +=1			
	

	# total_comment += count

print(f'Task completed!! Pics liked : {total_likes}; Comments : {total_comment}')
browser.quit()
