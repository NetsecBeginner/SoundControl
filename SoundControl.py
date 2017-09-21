#import curses for tui, alsaaudio for volume control
import curses, alsaaudio

#Initialize Curses and Alsa
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(1)

mixer = alsaaudio.Mixer()

#controls the system volume
class Volume:
	volume = int(mixer.getvolume()[0] / 20)
	
	
#Display Volume Slider, increase/decrease with input, pass value to curses
def main():
	while True:
		try:
			#Draw Screen
			displayScreen()

			#Get Keyboard Input
			kInput = screen.getch()
			
			if kInput == 261 and Volume.volume <= 20: #-->
				if Volume.volume != 20:
					Volume.volume += 1
			elif kInput == 260 and Volume.volume >= 0:#<--
				if Volume.volume != 0:
					Volume.volume -= 1
			elif kInput == 113: #Q
				exitApplication()
				
			#Sync Audio
			mixer.setvolume(Volume.volume * 5)
		except:
			exitApplication()

#Display Screen with volume slider
def displayScreen():
	screen.clear()
	screen.border(0)
	screen.addstr(12, 30, "[" + "#"*Volume.volume + "]")
	screen.refresh()


#Clean Up Curses and exit
def exitApplication():
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()
	exit()


#Call Main Function
main()
