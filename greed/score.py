class Score:
    
    score = 0
    
    
    """
    Nate

    Take the value from the objects class and update our score
    """
    #this code explains that when a gem gets close enough (hits)
    #the player, it will increase the score
def gem_hit():
    if gem.distance(player) < 15:
        score += 1
        print("Score: {}".format(score))
    
     #this code explains that when a rock gets close enough (hits)
    #the player, it will decrease the score  
def rock_hit():
    if rock.distance(player) < 15:
        score -= 1
        print("Score: {}".format(score))
