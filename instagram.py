'''
Instagram automation using python (c)Intzar
version 1.0


Features :-

> Automate following
> Automate Unfollowing
> Get users who are being followed by you but not following by them
> Get users who are common in your followers and following
> Get users who are not being followed by you
'''

from info import *
try:
    from selenium import webdriver
except:
    print('selenium module not found')
    op = input('Do you want to install selenium (y/n) :')
    if op == 'y':
        import os
        os.system('pip3 install selenium')
    elif op == 'n':
        print('Exiting...')
        import sys
        sys.exit()

from time import sleep

class insta:
    def __init__(self):
        self.username = username
        self.password = password
        self.otp = None
        self.NOT_FOLLOWING_BACK = 0
        self.COMMON_FOLLOWER_FOLLOWING = 1
        self.NOT_FOLLOWING_BACK_BY_ME = 2
        try:
            self.driver = webdriver.Chrome(chromedriver_path)
            self.driver.maximize_window()
            self.driver.get('https://instagram.com')
        except:
            print('-'*10+'ERROR'+'-'*10)
            print('chromedriver.exe not found\nPlease, enter correct chromedriver.exe path')
            op = input('Do you want to download chromedriver (y/n):')
            if op == 'y':
                print('Visit : https://chromedriver.chromium.org/downloads')
            elif op == 'n':
                print('Exiting...')

    def login(self,otp=False):
        self.otp = otp
        sleep(2)
        uname_field = self.driver.find_element_by_name('username')
        pass_field = self.driver.find_element_by_name('password')
        uname_field.send_keys(self.username)
        pass_field.send_keys(self.password)
        sleep(0.5)
        pass_field.submit()
        sleep(1)
        if self.otp == True:
            __otp = input('Enter OTP :')
            try:
                otp_filed = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input')
            except:
                otp_filed = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/div/label/input')
            otp_filed.send_keys(__otp)
            otp_filed.submit()
            sleep(2)

        sleep(2)
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        except:
            sleep(2)
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
            except:
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
                sleep(3)
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

        sleep(0.2)
    
    def profile(self, uname=None):
        if uname == None:
            self.driver.get(f'https://instagram.com/{self.username}')
            sleep(2)
        else:
            try:
                self.driver.get(f'https://instagram.com/{uname}')
                sleep(2)
            except Exception as e:
                print('-'*10+'ERROR'+'-'*10)
                print(e)
                print('-'*25)

    def unfollow(self,number=None,uname=None):
        if self.driver.current_url != f'https://www.instagram.com/{self.username}/':
            self.driver.get(f'https://www.instagram.com/{self.username}/')
        if uname != None:
            self.driver.get(f'https://www.instagram.com/{username}/')
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
            sleep(0.5)
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()

        else:
            try:
                follwing_count = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
                follwing_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
            except Exception as e:
                print('-'*10+'ERROR+'+'-'*10)
                print(e)
                print('-'*25)
            i, n, k= 0, (int(follwing_count)//10)+1, 1
            sleep(2)
            follwoing_scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
            while i<n:
                j=0
                if number is not None and k >= number:
                    break
                while j<10:
                    if number is not None and k >= number:
                        break
                    sleep(1)
                    try:
                        self.driver.find_element_by_xpath(f'/html/body/div[4]/div/div[2]/ul/div/li[{k}]/div/div[3]/button').click()
                    except:
                        try:
                            self.driver.find_element_by_xpath(f'/html/body/div[4]/div/div[2]/ul/div/li[{k}]/div/div[2]/button').click()
                        except:
                            break

                    sleep(1)

                    try:
                        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
                    except:
                        try:
                            self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[1]').click()
                        except:
                            break
                    k+=1
                    j+=1
                sleep(1)
                self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight)', follwoing_scroll_box)
                i+=1
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        
    def logout(self):
        if self.driver.current_url != f'https://www.instagram.com/{self.username}/':
            self.driver.get(f'https://www.instagram.com/{self.username}/')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/button[9]').click()
        sleep(2)

    def followers_following(self,option = 0):
        if self.driver.current_url != f'https://www.instagram.com/{self.username}/':
            self.driver.get(f'https://www.instagram.com/{self.username}/')
        sleep(2)
        followers = self.__getnames('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        following = self.__getnames('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        if option == 0:
            names = [name for name in following if name not in followers]
            print('Users who are not following back.')
        elif option == 1:
            names = [name for name in following if name in followers]
            print('Users who are common in followers and following.')
        elif option == 2:
            names = [name for name in followers if name not in following]
            print('Users who are not being followed by you.')
        else:
            print('Please Enter correct option')
            return
        names.sort()
        for name in names:
            print(name)

    def __getnames(self,xpath):
        sleep(1)
        try:
            count = self.driver.find_element_by_xpath(f'{xpath}/span').text
            btn = self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print('-'*10+'ERROR+'+'-'*10)
            print(e)
            print('-'*25)
        i, n = 0, int(count)//10+1
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        while i < n:
            sleep(1)
            self.driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight)',scroll_box)
            i+=1
        user_links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in user_links if name != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return names

    def follow(self,uname, number=1):
        if self.driver.current_url != f'https://www.instagram.com/{uname}/':
            self.driver.get(f'https://www.instagram.com/{uname}/')
        sleep(1)
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()
        except:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button').click()
        i=1
        k=3
        while i<number:
            sleep(1)
            try:
                self.driver.find_element_by_xpath(f'//*[@id="react-root"]/section/main/div/div[2]/div[2]/div/div/div/ul/li[{k}]/div/div/div/div/button[2]').click()
            except:
                try:
                    self.driver.find_element_by_xpath(f'//*[@id="react-root"]/section/main/div/div[1]/div[2]/div/div/div/ul/li[{k}]/div/div/div/div/button[2]')
                except:
                    print('Following Finished.')
                break
            k+=1
            i+=1
