clean:
	rm -rf ./build ./dist

build:
	pyinstaller ./hordeRL.py --add-data="./tiles.png:./tiles.png"