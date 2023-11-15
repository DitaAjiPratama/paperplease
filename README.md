# paperplease
Python Script for the token checking from cherrypy session.

It need `cherrypy` python library.

## Usage

Here is for set the token

  import paperplease
  paperplease.token_set("token", "xxxxxxxxxxxxxxx")

and here is for set the token

  import paperplease
  paperplease.token_check("token", "/login")
