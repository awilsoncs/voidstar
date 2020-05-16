all:
	make clean
	make build

clean:
	rm -rf ./build ./dist

clean-wd:
	rd /s /q .\build
	rd /s /q .\dist

build:
	pyinstaller ./hordeRL.py --add-data="./tiles.png:."

dist:
	pyinstaller ./hordeRL.py --add-data="./tiles.png:." -F

