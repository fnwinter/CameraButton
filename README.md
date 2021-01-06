# CameraButton
- Android Camera Button
    - 북스캔할 때 자동적으로 카메라 버튼 눌러주는 프로그램

## 필요한 프로그램
- vFlat [Link to Store](https://play.google.com/store/apps/details?id=com.voyagerx.scanner)
- Optional : Chocolatey [Link](https://chocolatey.org/)
- Android platform-tools
    - choco install adb
- scrcpy [Github Link](https://github.com/Genymobile/scrcpy)
    - choco install scrcpy

## 사용법
- Connect : adb 연결
- Remote connection : 같은 공유기망에서 무선으로 접속(유선 연결 후 케이블 제거)
- Kill server : 접속이 안될 때 adb 서버 재시작
- scrcpy : 안드로이드 화면 보여주는 프로그램 실행 (실행한 해줌)
- Capture : 카메라 버튼 눌러줌
- Tick : 카메라 버튼 시간 간격 (초)
- Start/Stop : 타이머 시작 / 중지

## 다운로드
- [Link](https://github.com/fnwinter/CameraButton/blob/main/source/dist/CameraButton.exe)
    - 윈도우에서 위험하다고 경고 뜨지만 무시하고 실행하세요. 아니면 build.sh 돌려서 직접 빌드 하셔도 됩니다.
    - 이름: CameraButton.exe
    - 크기: 8725100 바이트 (8520 KiB)
    - SHA256: 615F2F0CFCC04320D7BCCF4051D16A8ADD4CA0FD6236AED4337DCC23911A535F

## 스크린샷
![](https://github.com/fnwinter/CameraButton/blob/main/images/screenshot.JPG?raw=true)