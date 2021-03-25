def password_generator(username):
  password = ""
  n = 0
  while n<len(username):
    password += username[n-1]
    n += 1
  return password
val = password_generator("Talha")
print(val)
print("what thr ")

