# 백내장 데이터셋 train, validation, test 분류 코드

import os
import shutil
import random

def split_data(source_folder, train_folder, val_folder, test_folder, train_ratio=0.7, val_ratio=0.1, test_ratio=0.2):
    # 폴더가 없다면 생성
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # 이미지 파일 목록 가져오기
    files = [f for f in os.listdir(source_folder) if f.endswith(('jpg', 'jpeg', 'png'))]  # 이미지 파일만 필터링
    random.shuffle(files)  # 파일 섞기

    # 비율에 맞게 분할할 인덱스 계산
    total_files = len(files)
    train_end = int(total_files * train_ratio)
    val_end = train_end + int(total_files * val_ratio)

    # 파일을 각 폴더로 이동
    for i, file in enumerate(files):
        source_path = os.path.join(source_folder, file)
        if i < train_end:
            shutil.copy(source_path, os.path.join(train_folder, file))
        elif i < val_end:
            shutil.copy(source_path, os.path.join(val_folder, file))
        else:
            shutil.copy(source_path, os.path.join(test_folder, file))

    print(f"데이터 분할 완료: {len(files)}개의 파일을 {train_folder}, {val_folder}, {test_folder}로 나누었습니다.")

# 예시: 이미지 파일을 'source_folder'에서 'train', 'val', 'test' 폴더로 나누기
source_folder = r'C:\Users\User\PycharmProjects\deepLP\eye\원천데이터\백내장\초기'  # 이미지가 들어있는 폴더 경로
train_folder = r'C:\Users\User\PycharmProjects\deepLP\eye\원천데이터\백내장\초기\train'
val_folder = r'C:\Users\User\PycharmProjects\deepLP\eye\원천데이터\백내장\초기\val'
test_folder = r'C:\Users\User\PycharmProjects\deepLP\eye\원천데이터\백내장\초기\test'

split_data(source_folder, train_folder, val_folder, test_folder)
