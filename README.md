This is a webapp that creates bingo cards from a list of prompts. The intended use case is fandom writing events; currently it is set up with the prompt list and other fandom-specific items hardcoded in. Eventually I'd like to learn how to make a database and turn it into a service that bingo admins could use to enter their prompts and then send out a generation link to participants. 

To try it out, install flask and run `flask --app bingo run` in the top-level directory. 

Change the prompt list on line 14 of bingo.py. Change the landing page title and free space option on lines 5 and 20 of templates/form.html
