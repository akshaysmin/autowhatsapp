# autowhatsapp
automate messaging with whatsapp and logging friends' statuses

## Requirements:
selenium python module, firefox webdriver

I'm working on it.
## Current usages:
>To log status info like time and no. of staus for each friend
Run status_logger.py from command line. 

This opens whatsapp web website. Scan the QR code using your whatsapp, then click to view status list. Now press Enter in the terminal as prompted to record status info on the file "status_log.dat"

## for people who want to work on this:
autowhatsapp.py and status_log.py are main files.
Others are parts of their code.
geckodriver.exe is neccessary
notes_for_autowhatsapp.txt maybe helpful for development


autowhatsapp.py -> send given message to given contact with customisations
status_log.py   -> log status info of all friends with customisations

what are customisations ? Anything imaginable
