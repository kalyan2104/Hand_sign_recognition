import os
# Get the current working directory
current_dir = os.getcwd()
# Create a new directory
# 'testdir' in the current working directory
os.mkdir('testdir')
# Change the current working directory
# to the newly created directory
os.chdir('testdir')
# Get the current working directory
new_dir = os.getcwd()
# Prints the current working directory
# and the newly created directory
print(current_dir)
print(new_dir)
# Create a new file in the new directory
open('test.txt','w')
# List the contents of the current directory
print(os.listdir('.'))
# Change the current working directory
# back to the original directory
os.chdir(current_dir)
# Delete the newly created directory
# and all its contents
os.rmdir('testdir')
