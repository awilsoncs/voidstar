all:
	make clean
	make dist

clean:
	powershell "Remove-Item -r -fo -ErrorAction Ignore .\dist; $$null"
	powershell "Remove-Item -r -fo -ErrorAction Ignore .\build; $$null"

build:
	pyinstaller ./hordeRL.py --add-data="./tiles.png:."

dist:
	pyinstaller ./dist.spec

push:
	butler push .\dist\oh-no-its-the-horde.exe jazzbox/oh-no-its-the-horde:windows-x64 --userversion 0.5.0
