# mapBot
This is a Discord Bot that utilizes POSTGRES SQL and DISCORD.py to create a bot</h2>
<p>The bot helps in the selection of maps and host.  It also is capable of displaying the information so users can quickly reference the nights current maps</p>

<h2>Libraries Used In Project</h2>
<ul>
<li>import random</li>
<li>from datetime import datetime</li>
<li>import pytz</li>
<li>import numpy as np</li>
<li>import psycopg2</li>
<li>from discord.ext import commands</li>
</ul>


<h2>Current Commands Available with the prefix of "."</h2>
<h3>USER COMMANDS</h3>
<ul>
  <li>displayHost - Displays all possible hosts</li>
  <li>setHost - Sets the host</li>
</ul>
<h3>MAP COMMANDS</h3>
<ul>
  <li>displayMaps -  Displays the current maps to be played</li>
  <li>setMap - sets map 1, 2, or 3 and map by ID</li>
  <li>setMapsRandom - Sets three random maps (use arguments of 3, 4, or 5 to pull from a map_count of the same number)</li>
  <li>vsMaps - Displays all vs maps with ID</li>
</ul>
<h3>CLEAR COMMANDS</h3>
<ul>
  <li>clearHost - Clears the host entry</li>
  <li>clearMap - Clears map 1, 2, or 3</li>
  <li>clearMaps - Clears the maps</li>
  <li>clearAll  - Clears maps and the host</li>
</ul>
<h3>MISC COMMANDS</h3>
<ul>
  <li>gameTime - Displays current time and game time</li>
  <li>help - Displays command help</li>
</ul>

<h2>Resources:</h2><ul>
<li><a href = "https://www.python.org/">Python</a></li>
<li><a href = "https://www.jetbrains.com/pycharm/">PyCharm Python IDE</a></li>
<li><a href = "https://www.pgadmin.org/">PGADMIN PostgresSQL</a></li>
<li><a href = "https://discord.com/developers/applications">Discord Applications</a></li>
<li><a href = "https://www.postgresqltutorial.com/">Postgres SQL Tutorial</a></li>
<li><a href="https://www.w3schools.com/python/default.asp">Python and numpy tutorial</a></li>
<li><a href="https://towardsdatascience.com/creating-a-discord-bot-from-scratch-and-connecting-to-mongodb-828ad1c7c22e">Creating a Discord Bot tutorial</a></li>

