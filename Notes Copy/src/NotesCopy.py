import os
import time

print "Copying your notes..." + "\n"
print "Close this if you still want to make changes\n"
time.sleep(2)

for countdown in range(3, 0, -1):
    print "... %s" % countdown
    time.sleep(1)
    

notes_location = "insert file dir that contains the notes"
save_location = 'insert saved dir/#1Copied Notes.txt'           #you may change the #1Copied Notes.txt 
    

try:
    os.remove('insert saved dir/#1Copied Notes.txt')            #put the same name here
    print "\nDeleting the old note...\n"
    time.sleep(1)
except:
    print "\nCopying the file...\n"
    time.sleep(1)
    



for root, dirs, files in os.walk(notes_location):

    for file in files:
        item = os.path.join(root, file)

        if item.endswith('.txt'):
            take_file = open(item, 'r')
            copy_file = open(save_location, 'a')
            for line in take_file:
                copy_file.write(line)
            copy_file.write("\n\n" + ("=" * 70) + "\n\n")
            take_file.close()
            copy_file.close()

print "Copy Complete"
time.sleep(1.5)