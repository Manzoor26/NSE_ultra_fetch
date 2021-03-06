"""__main__production__code   Princess Leia, i have no idea why i named it. Pulls the data from NSE which is EOD data.
				------------------pulls  data------------------ 
"""

import datetime
import time
import schedule
import requests
import os, zipfile,sys,shutil
from os import listdir
from os.path import isfile, join
from datetime import datetime
from anubis_main import *      

file_path = os.getcwd()
directory_to_bhav = file_path + '/BHAV_CPY/'					
directory_to_oi = file_path +'/OI/' 				
directory_to_vol = file_path + '/VOLATILITY/'

day=datetime.now().date().strftime ("%d")         #.strftime ("%Y%m%d") ###for fetching the current date and strips the needed 
month=datetime.now().date().strftime ("%m")


list_of_months = ['unindex','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
month_in_words = list_of_months[int(month)]


def Bhav_Cpy(month_var,day_var):
	month_temp = month_var            #str
	day_temp = day_var		  #int
	
	def Bhav_Cpy_mental():
			if (day_temp<=9):
				url='http://www.nseindia.com/content/historical/DERIVATIVES/2017/{}/fo{}{}2017bhav.csv.zip'
				
				r = requests.get(url.format(month_temp,day_temp,month_temp))	
				file_name="fo{}{}2017bhav.zip"
				modified_f_name=file_name.format(day_temp,month_temp)      #file name you want for the incoming to be saved as

				###os.path.join is used to merge the creating .zip files into the current /bhav_cpy dir
				with open(os.path.join(directory_to_bhav,modified_f_name), "wb") as code: 
						code.write(r.content)  

			else:
				url='http://www.nseindia.com/content/historical/DERIVATIVES/2017/{}/fo{}{}2017bhav.csv.zip'
				r = requests.get(url.format(month_temp,day_temp,month_temp))	
				file_name="fo{}{}2017bhav.zip"
				modified_f_name=file_name.format(day_temp,month_temp)
				with open(os.path.join(directory_to_bhav,modified_f_name), "wb") as code:
						code.write(r.content)			

	if not os.path.exists(directory_to_bhav):
		os.mkdir(directory_to_bhav)
		Bhav_Cpy_mental()
	else:
		print "ELse part"
		Bhav_Cpy_mental()


def Open_Interest(month_in_num_var,day_var):
	month_temp = month_in_num_var     		  #int
	day_temp = day_var				  #int
	
	def Open_Interest_mental():
			if (day_temp<=9):
				url='https://www.nseindia.com/archives/nsccl/mwpl/nseoi_{}{}2017.zip'
				
				r = requests.get(url.format(day_temp,month_temp))	
				file_name="nseoi_{}{}2017.zip"
				modified_f_name=file_name.format(day_temp,month_temp)

				###os.path.join is used to merge the creating .zip files into the current /bhav_cpy dir
				with open(os.path.join(directory_to_oi,modified_f_name), "wb") as code: 
						code.write(r.content)  

			else:
				url='https://www.nseindia.com/archives/nsccl/mwpl/nseoi_{}{}2017.zip'
				
				r = requests.get(url.format(day_temp,month_temp))	
				file_name="nseoi_{}{}2017.zip"
				modified_f_name=file_name.format(day_temp,month_temp)
				with open(os.path.join(directory_to_oi,modified_f_name), "wb") as code:
						code.write(r.content)

	if not os.path.exists(directory_to_oi):
		os.mkdir(directory_to_oi)
		Open_Interest_mental()
	else:
		print "ELse part"
		Open_Interest_mental()	


def Volatility(month_var,day_var):
	month_temp = month_var           		  #str
	day_temp = day_var				  #int
	
	def Volatility_mental():
			if (day_temp<=9):
				url='https://www.nseindia.com/archives/nsccl/volt/FOVOLT_{}{}2017.csv'
				
				r = requests.get(url.format(day_temp,month_temp))	
				file_name="fovolt_{}{}2017.csv"
				modified_f_name=file_name.format(day_temp,month_temp)

				###os.path.join is used to merge the creating .zip files into the current /bhav_cpy dir
				with open(os.path.join(directory_to_vol,modified_f_name), "wb") as code: 
						code.write(r.content)   

			else:
				url='https://www.nseindia.com/archives/nsccl/volt/FOVOLT_{}{}2017.csv'

				r = requests.get(url.format(day_temp,month_temp))	
				file_name="fovolt_{}{}2017.csv"
				modified_f_name=file_name.format(day_temp,month_temp)

				with open(os.path.join(directory_to_vol,modified_f_name), "wb") as code:
						code.write(r.content)			

	if not os.path.exists(directory_to_vol):
		os.mkdir(directory_to_vol)
		Volatility_mental()
	else:
		print "ELse part"
		Volatility_mental()



def Unzipper(unzip_directory):
	file_path=os.getcwd()
	
	###listdir is used to list the contents of a directory
	onlyfiles = os.listdir(unzip_directory)

	for i in onlyfiles:
		path_to_zipfile= unzip_directory + "/{}".format(i)
		
		###refer zipfile doc for more info about the underlying function
		zip = zipfile.ZipFile(path_to_zipfile, 'r')
		zip.extractall(unzip_directory)
		zip.close()



def Full_Clean():
	directory =[directory_to_bhav,directory_to_vol,directory_to_oi] 
	
	for i in range(len(directory)):
	    test = os.listdir( directory[i] )
	    removable_file = (".zip",".xml")
		
	    for item in test:
	        if item.endswith(removable_file):
	            os.remove(os.path.join(directory[i], item ))


###custom function for pulling particular date
def Groupping():									
	Bhav_Cpy(month_in_words,day)			#(month,day) ("str(first three letter of the month)",int)
	Unzipper (directory_to_bhav)
	Open_Interest(month,day)			#(month,day) (int,int)
	Unzipper(directory_to_oi)     
	Volatility(month,day)				#(month,day)  (int,int)
	Full_Clean()

###contains the link defn to all the proper flow  ****do not modify **** 
def Godzilla():										
	if not os.path.exists(directory_to_bhav):
		Groupping()
		print "=====Running Princess Leia====="
	else:
		shutil.rmtree(directory_to_bhav)
		shutil.rmtree(directory_to_vol)
		shutil.rmtree(directory_to_oi)
		print "=====Running Princess Leia====="
		Groupping()	

###SCHEDULER CALLS ALL THIS FUNCTION AT THE PREDEFINED TIME https://schedule.readthedocs.io/en/stable/

schedule.every().monday.at("17:29").do(Godzilla)		###for Indian users change time to 19:29
schedule.every().monday.at("17:30").do(Bitch_Pls_Trigger)	###for Indian users change time to 19:30 

schedule.every().tuesday.at("17:29").do(Godzilla)
schedule.every().tuesday.at("17:30").do(Bitch_Pls_Trigger)

schedule.every().wednesday.at("17:29").do(Godzilla)
schedule.every().wednesday.at("17:30").do(Bitch_Pls_Trigger)

schedule.every().thursday.at("17:29").do(Godzilla)
schedule.every().thursday.at("17:30").do(Bitch_Pls_Trigger)

schedule.every().friday.at("17:29").do(Godzilla)
schedule.every().friday.at("17:30").do(Bitch_Pls_Trigger)

#schedule.every().day.at("22:18").do(Godzilla)
#schedule.every().day.at("22:19").do(Bitch_Pls_Trigger)	

if __name__ == '__main__':
	while True:
		schedule.run_pending()
		time.sleep(1)
