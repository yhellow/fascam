# Section03
# python venv fundamentals, settings, pip usage, connecting vscode 
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

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
"""
    가상환경에서 샘플 패키지 설치해보기
    1. source ./activate
        !! pip 업그레이드: 'pip install --upgrade pip'
    2. 원하는 파이썬 확장패키지가 있는지 pip 에 검색해본다: 'pip search packageName'
        !! 검색어가 들어간 확장패키지 검색: 'pip search searchWord*'
    3. pip 에서 확장패키지 설치하기: 'pip install packageName'
    4. pip 에서 확장패키지 제거하기: 'pip uninstall packageName'
    5. 현재 가상환경에 설치되어있는 확장패키지 나열: 'pip list'
        !! 확장패키지 업그레이드: 'pip install --upgrade packageName'
    6. 설치한 확장패키지에 대한 정보: 'pip show packageName'
        !! 확장패키지 설치 후 import 가 안될 경우 vscode 재시작
"""


# Testing installed package

import simplejson as json

test_dict = {'1': 95, '4': 77, '3': 65, '5': 100, '2': 88}

#simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))
