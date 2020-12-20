email = input("e-mail adresi giriniz..")
is_email = False
for char in email:
   if char == "@": # @ karakteri varsa e-mail'dir
      is_email = True

if is_email:
   print("e-mail'dir")
else:
   print("e-mail değildir")