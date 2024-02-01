# Card games project

**Games**

The project was created in order to practice working with OOP, databases, web framework.


Project Objectives:

 - Realization of game logic
 - Simulation of games (such as blackjack & poker)
 - Using databases (non-relational)
 - html/css layout
 - Writing processing functions in js
 - Building APIs with Python [fastAPIs](https://fastapi.tiangolo.com)
 - Js interfacing with python
 - Working with visual component of the site

### current game realised:
+ [Blackjack](https://en.wikipedia.org/wiki/Blackjack) (in process)


### Project structure:

    < PROJECT ROOT >
       |
       |    |-- application.py              # Game app
       |    |
       |    |-- api/                   
       |    |    |-- routing.py             # pages router
       |    |    |-- settings.py            # project setting
       |    |    |-- srv.py                 # server start point
       |    |    |
       |    |-- core/                  # Game logic
       |    |    |   Bank.py           # Bank
       |    |    |   Blackjack.py      # logic of blackjack game
       |    |    |   Deck.py           # Deck, Hand, Card 
       |    |    |
       |    |-- frontend/              # js, staticfiles, templates
       |        
       |-- ************************************************************************

