all:
	make clean
	make build

clean:
	rm -rf ./build ./dist
	rm ./horde.tar

build:
	pyinstaller ./hordeRL.py --add-data="./tiles.png:."

dist:
	pyinstaller ./hordeRL.py --add-data="./tiles.png:." -F
	cp ./README.md ./dist/README.md
	tar -cvf ./horde.tar ./dist/

deploy:
	make clean
	make dist
	butler push ./horde.tar jazzbox/oh-no-its-the-horde:linux-universal
