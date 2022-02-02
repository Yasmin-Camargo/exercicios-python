from pygame import mixer

print ('\nOuça meu podcast sobre a história de algumas mulheres negras na computação:\n\n')
mixer.init()
mixer.music.load('./podcast.mp3')
mixer.music.play()
x = input('Digite algo para parar...')
