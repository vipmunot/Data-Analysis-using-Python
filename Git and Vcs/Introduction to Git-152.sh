## 1. Version control systems ##

/home/dq$ git init random_numbers

## 2. The .git folder ##

/home/dq$ ls -al

## 3. Creating some files ##

/home/dq$ mv script.py random_numbers/

## 4. Git status ##

/home/dq/random_numbers$ git add README.md

## 5. Configuring git ##

/home/dq/random_numbers$ git config --global user.name "Vipul Munot"

## 6. Committing ##

/home/dq/random_numbers$ git commit -m "Intial commit. Added Script.py and READ

## 7. File differences ##

/home/dq/random_numbers$ git status

## 8. Making a second commit ##

/home/dq/random_numbers$ git commit -m "Added random generator code"

## 9. Looking at the commit history ##

/home/dq/random_numbers$ git log

## 10. Seeing commit differences ##

/home/dq/random_numbers$ git log --stat