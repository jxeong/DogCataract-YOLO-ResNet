# YOLOv8 + ResNet-18 두 모델을 사용한 반려견 백내장 진단 딥러닝 모델 README
딥러닝 플랫폼 기말 프로젝트

## 🐶 프로젝트 소개
- 목표: **반려견 백내장 조기 진단을 위한 딥러닝 모델 개발**
- YOLOv8으로 반려견 눈 영역을 검출하고, ResNet-18로 백내장 진행 단계를 ‘정상-초기-비성숙-성숙’으로 분류하는 딥러닝 시스템
- 각각의 모델은 강아지 얼굴 데이터셋과 백내장 데이터셋을 사용해 별도로 학습

## 📌 데이터셋 다운로드, 폴더 위치
- [YOLO] 강아지 얼굴 - 눈 데이터셋(이미지, 라벨링) -<a href="https://drive.google.com/file/d/1Kpyr5NNtKyTtM7oFbv-JW4uux3fkFRy4/view?usp=sharing" > 구글드라이브 이동</a>
     - YOLO 데이터셋 파일 경로: `ultralytics/custom_train`

- [ResNet] 반려견 백내장 진행 단계 데이터셋(이미지) -<a href="https://drive.google.com/file/d/16yyHc9qtFL8t1XJTO6o2_pUhwn8J6wNV/view?usp=sharing" > 구글드라이브 이동</a>
     - ResNet 데이터셋 파일 경로: `eye/eye_data`

## 💡 실행 방법
### YOLOv8 학습, 실행 코드
- `/ultralytics` 폴더에서 터미널로 실행
- 학습: `yolo train cfg=custom_train/custom_train_cfg.yaml device=0`
- 테스트: `yolo val model=runs/detect/train4/weights/best.pt data=custom_train/custom_dataset.yaml split=test iou=0.5`
- 새로 학습한 가중치로 테스트 하고 싶을 경우, 테스트 코드의 `train{number}` 변경해야 함

### ResNet-18 실행 파일
- `ResNet_SGD.ipynb` 파일 `jupyter-notebook`으로 실행(VSC도 무관)
- 테스트: `best_resnet_copy2` 가중치 파일로 테스트 가능

### ⚙️ 개발 환경
- GPU: `NVIDIA GeForce RTX 3060 Ti`
- `Pycharm` 가상환경

## 📁 프로젝트 구조
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
     │     │    ├── images
     │     │    └── labels
     │     └── test
     │          ├── images
     │          └── labels
     │          .
     │          .
     │          .
```

