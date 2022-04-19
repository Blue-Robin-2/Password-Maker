import random
import os



class Passwordmaker:
  def __init__(self):
    self.chars_list = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

  
  def random_str(self,length):
    print('This can be used to create passwords!')
    self_chars = []
    self_string = ""
    #make list of random items
    for i in range(int(length)):
      try:
        print(round((i/int(length)) * 100), '% done', end = "\r")
      
      except ZeroDivisionError:
        print(0, end = "\r")
      random_self = round(random.randrange(0,len(self.chars_list)))
      self_chars.append(self.chars_list[random_self])
    print('Part one complete.')
    #make list into a string      
    for i in range(len(self_chars)):
      self_string = self_string + str(self_chars[i])
      try:
        print(round(i/(float(len(self_chars))) * 100), 'Percent done', end = "\r")
      except ZeroDivisionError:
        print(0, end = "\r")
      

    return self_string
