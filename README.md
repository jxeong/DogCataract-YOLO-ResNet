# DogCataract-YOLO-ResNet
YOLOv8 + ResNet-18 두 모델을 사용한 반려견 백내장 진단 딥러닝 모델 개발 기말 프로젝트


## 🖥️ 프로젝트 소개
본 프로젝트는 YOLOv8으로 반려견 눈 영역을 검출하고, ResNet-18로 백내장 진행 단계를 ‘정상-초기-비성숙-성숙’으로 분류하는 딥러닝 시스템을 개발하였다. 각각의 모델은 강아지 얼굴 데이터셋과 백내장 데이터셋을 사용해 별도로 학습되었다.
<br>

### ⚙️ 개발 환경
- `Java 8`
- `JDK 1.8.0`
- **IDE** : STS 3.9
- **Framework** : Springboot(2.x)
- **Database** : Oracle DB(11xe)
- **ORM** : Mybatis

### 📌 데이터셋 다운로드, 폴더 위치
- [YOLO] 강아지 얼굴 - 눈 데이터셋(이미지, 라벨링) -<a href="https://drive.google.com/file/d/1Kpyr5NNtKyTtM7oFbv-JW4uux3fkFRy4/view?usp=sharing" > 구글드라이브 이동</a>
- YOLO 데이터셋 파일 경로: `ultralytics/custom_train`

- [ResNet] 반려견 백내장 진행 단계 데이터셋(이미지) -<a href="https://drive.google.com/file/d/16yyHc9qtFL8t1XJTO6o2_pUhwn8J6wNV/view?usp=sharing" > 구글드라이브 이동</a>
- ResNet 데이터셋 파일 경로: `eye/eye_data`

### 📌 프로젝트 구조

```
├── README.md
├── requirements.txt
│
└── eye
     ├── 00_train_val_test.py
     ├── ResNet_Adam.ipynb
     ├── ResNet_SGD.ipynb
     ├── best_adam_resnet.pth
     ├── best_resnet_copy2.pth
     ├── pylib.py
     └── eye_dataset
           ├── train
           ├── val
           └── test
└── ultralytics
     ├── runs
     │     └── detect
     │          ├── train4
     │          ├── val8
     │          └── val9
     │               .
     │               .
     │               .
     ├── custom_train
     │     ├── custom_dataset.yaml
     │     ├── custom_train_cfg.yaml
     │     ├── custom_yolov8.yaml
     │     ├── train
     │     │    ├── images
     │     │    └── labels
     │     ├── valid
     │     └── test
     │          .
     │          .
     │          .
```



## 📌 주요 기능
#### 로그인 - <a href="https://github.com/chaehyuenwoo/SpringBoot-Project-MEGABOX/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(Login)" >상세보기 - WIKI 이동</a>
- DB값 검증
- ID찾기, PW찾기
- 로그인 시 쿠키(Cookie) 및 세션(Session) 생성
