def combat(health, damage):
  new_health = health - damage
  return max(0, new_health)  
