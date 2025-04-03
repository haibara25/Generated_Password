from generate import password
file_path='password.txt'
with open(file_path,'w') as file :
    file.write(password)
