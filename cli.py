import animator
import sys
import locale

try:
	if sys.argv[1] == "-h":
		print(f"{__file__} <dosya>: Animasyonu Oynatır")
	else:
		ani=animator.Animator()
		ani.scenes_from_file(sys.argv[1])
		ani.play()
except IndexError:
	if locale.getdefaultlocale()[0]  == "tr_TR":
		print("Lütfen bir argüman girin. Yardım almak için -h")
	else:
		print("Please enter an argument. -h to get help")