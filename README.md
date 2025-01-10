# IsaacSim과 Conty3.x 연동 방법

## 개요

Conty3.0과 IsaacSIM 시뮬레이터를 연동하기 위한 방법입니다. 사용 시 문의 사항이나 버그 발생 시 아래 담당자에게 연락해 주시기 바랍니다.

* 담당자: 이윤동 매니저

#### [아이작심 다운로드](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/index.html) ※ Isaac Sim V4.0.0 사용 필요

## neuromeka-isaacsim 패키지 설치
* pip를 사용하여 neuromeka-isaacsim 패키지를 설치합니다.
```bash
pip3 install neuromeka-isaacsim
```
* 다음 명령어를 통해 Isaac Sim에서 불러올 수 있는 .usd 파일과 usd 파일에서 사용되는 extension 폴더를 설치합니다.
```bash
neuromeka-isaacsim-install
```

## STEP에서 스크립트 실행하기

Isaac Sim과 Conty를 연동하기 위해서는 로봇을 실행해야 합니다.

#### SSH 터미널 및 파일 전송 프로그램 (무료): [MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html)

### STEP 터미널 접속
>![MobaXterm 초기 화면](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/coppeliasim/MobaXterm_SSH_%EC%97%B0%EA%B2%B0.png)  
시뮬레이션을 실행할 STEP의 IP 주소를 입력하여 STEP에 접속합니다.

### STEP의 Username, Password 입력
>![MobaXterm 로그인 화면](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/coppeliasim/ID_PW.png)  
(login as : root, password : root)

### 시뮬레이션 로봇 설정
시뮬레이션을 위해선 EtherCAT 통신을 비활성화 해야합니다.
```bash
cd /home/user/release/IndyDeployment/
```
>![Deployment경로](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/coppeliasim/Deployment%EA%B2%BD%EB%A1%9C.png)  
1. 좌측 하단의 Follow terminal folder 버튼을 체크하여 폴더 구조를 확인합니다.

>![indyDeploy.json](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/coppeliasim/indyDeploy_json.png)
2. indyDeploy.json 파일을 열어 EtherCATCommTask의 Enable 값을 0으로 설정하고 저장합니다.  



### 파이썬 스크립트 실행
프레임워크 실행
```bash
python3 /home/user/release/IndyDeployment/indy_run.py  
```

## Isaac Sim 상에서 실행하기

### Extension 활성화
Isaac Sim과 Conty를 연동하는 데 필요한 Extension을 활성화해야 합니다.

>![Extensions 위치](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/isaacsim/extensions+%EC%9C%84%EC%B9%98.png)  
Isaac Sim 상단 메뉴 바의 **Window - Extensions**을 클릭하여 Extensions 윈도우를 엽니다.

>![Extension Autoload 설정](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/isaacsim/extension+autoload+%EC%84%A4%EC%A0%95.png)  
Extensions 윈도우에서 왼쪽 창의 **THIRD PARTY** 탭을 선택하고, **omni.isaacsim_bridge.extension**이 있는 Extension을 클릭합니다.  
브릿지 Extension의 활성화를 위해 오른쪽 창에서 DISABLED를 **ENABLED** 상태로 바꾸고, **AUTOLOAD** 체크박스에 체크합니다.

### conty_bridge.usd 실행 및 STEP과 연결
>![USD 경로](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/isaacsim/USD+%EA%B2%BD%EB%A1%9C+%EC%B0%BE%EA%B8%B0.png)  
Isaac Sim 하단의 Content 창의 Path를 입력하는 창에 `C:\Users\<user name>\neuromeka-isaacsim`을 입력합니다.  
해당 경로에 있는 파일 중 **conty_bridge.usd** 파일을 더블 클릭하여 불러옵니다.

### Step IP 입력하기
>![STEP과 연결](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/isaacsim/USD+%EC%8B%A4%ED%96%89+%EC%9D%B4%ED%9B%84+STEP+IP+input.png)  
conty_bridge.usd 파일이 로드되면 오른쪽 창 Stage 탭이 업데이트됩니다.
업데이트 된 Stage 탭에서 **ActionGraph** 하위의 **isaacsimbridge**를 클릭합니다.  
클릭하면 우측 하단 Property 탭이 업데이트 되고, Isaac_sim_bridge Node의 Inputs 안에 있는 **StepIP**에 STEP IP를 입력합니다.

### 재생 버튼 클릭 후, Conty 3.x으로 로봇 제어하기
>![실행](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/isaacsim/%EC%8B%A4%ED%96%89.png)
실행 버튼을 클릭하면 콘티와 실시간으로 연결됩니다.

>![실행 중](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/isaacsim/%EC%8B%A4%ED%96%89+%EC%A4%91.png) ![실행 중](https://s3.ap-northeast-2.amazonaws.com/internal.neuromeka.com/images/isaacsim/Conty+3.x+%EB%A1%9C%EB%B4%87+%EC%A0%9C%EC%96%B4.jpg)
Conty 3.x로 로봇을 조작하면 실시간으로 Isaac Sim에서 렌더링되는 것을 확인할 수 있습니다.
