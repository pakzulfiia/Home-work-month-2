class Streamer:    
  def live(self):       
    return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
  def earn(self):       
    return "Заработал 500 донатов за 2 часа"

class TikToker:    
  def live(self):        
   return "Снимаю трендовый тикток под песню месяца!"
  
  def viral(self):        
      return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:    
  def live(self):        
    return "Я... я свечусь в темноте... это мой вайб..."
    
  def superpower(self):       
    return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
  def ultimate_content(self):
    print(f'{self.earn()}, {self.superpower()}, я GlowStreamer')

class ViralCyborg(TikToker, Mutant):
  def ultimate_content(self):
    print(f'{self.viral()}, {self.superpower()}, я ViralCyborg')

class DonateMage(Streamer, TikToker):
  def ultimate_content(self):
    print(f'{self.earn()}, {self.viral()}, я DonateMage')


mage = DonateMage()
mage.ultimate_content()
print(DonateMage.__mro__)

cyborg = ViralCyborg()
cyborg.ultimate_content()
print(ViralCyborg.__mro__)

streamer = GlowStreamer()
streamer.ultimate_content()
print(GlowStreamer.__mro__)
print()

together =[mage, cyborg, streamer]
for they in together:
  print(they.live())
  they.ultimate_content()