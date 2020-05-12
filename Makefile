all:
	make clean
	make build

clean:
	rm -rf ./build ./dist

build:
	pyinstaller ./hordeRL.py --add-data="./tiles.png:."

dist:
	pyinstaller ./hordeRL.py --add-data="./tiles.png:." -F

