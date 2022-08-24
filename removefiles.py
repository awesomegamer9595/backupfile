import os
import shutil
import time
def main():
     path1= input("enter the path")
     days=int(input("how old do you want your files to be"))
     deleted_folders=0
     deleted_files=0
     # time.time returns the amount of time in seconds from jan 6,1981
     seconds = time.time()-(days*24*60*60)

     exist = os.path.exists(path1)

     if exist is True:
          
      for root_folder,folders,files in os.walk(path1):
          if seconds >= get_age(root_folder):
               remove_folders(root_folder)
               deleted_folders=deleted_folders +1
               break
          else:
               for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds >= get_age(folder_path):
                         remove_folders(folder_path)
                         deleted_folders=deleted_folders +1
               for file in files:
                      file_path=os.path.join(root_folder,file)
                      if seconds >= get_age(file_path):
                         remove_files(file_path)
                         deleted_files=deleted_files +1
     else:
          print("file not found")
          
     print(deleted_folders,deleted_files)
                    

                           

def remove_files(path1):
     if not os.remove(path1):
          print("file deleted")
     else:
          print("file delete failed")

def remove_folders(path1):
     if not shutil.rmtree(path1):
          print("folder deleted")
     else:
          ("folder not deleted")

def get_age(path1):
     ctime=os.stat(path1).st_ctime

     return ctime

main()