""" 
    가상환경의 필요성: 
    환경변수에 의한 오류 혹은 호환성 문제를 지양하기 위해 각각 필요한 버전을 입혀주는 툴
    각 프로젝트마다의 환경을 만들어 생성/제거가 순조롭도록 도와주며 프로젝트 관리에 유용
    
    가상환경 설정 및 패키지 설치 + 실행:
    1. go to preferred file on terminal
    2. 'python3 -m venv (existingfilename)/(newfilename)'
    3. created files -- lib, include, bin, !!pyvenv.cfg
    # bin(binary) folder contains the file that activates/deactivates the venv
    4. cd bin
    5. 진입 activate: 'source ./activate'
    6. 해제 deactivate: 'source ./deactivate' / 'deactivate'

    pip 명령어 : search , install, uninstall, list, freeze, show
	pip install search simplejson , simple*
	pip install install simplejson
	pip install install simplejson==버전
	pip install --upgrade simplejson
	pip show simplejson
	pip show -f simplejson
	pip freeze > packages.txt
	pip freeze --all > packages.txt
	pip install -r packages.txt

	python -m venv /path/to/venv

	command : code 실행
"""