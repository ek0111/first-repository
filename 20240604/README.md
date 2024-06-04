##🔑 **PRT(Peer Review Template)**

### [ ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개,
      1. 자기만의 카메라앱 기능 구현을 완수하였다.
          - [ ] 얼굴 영역과 랜드마크를 정확하게 검출하고, 스티커 사진을 합성시키는 데 성공하였다.
      2. 스티커 이미지를 정확한 원본 위치에 반영하였다.
          - [ ] 정확한 좌표계산을 통해 고양이 수염의 위치가 원본 얼굴에 잘 어울리게 출력되었다.
          
      3. 카메라 스티커앱을 다양한 원본이미지에 적용했을 때의 문제점을 체계적으로 분석하였다.
          - [ ] 얼굴각도, 이미지 밝기, 촬영거리 등 다양한 변수에 따른 영향도를 보고서에 체계적으로 분석하였다.
              - 문제점에 대해서 생각을 해봤지만, 문제에 대한 실험을 수행하는 부분이 빠져 아쉬웠습니다.

### [ ]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
    - [x] Step 1. 스티커 구하기 or 만들기
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/e2e71e47-2e64-42cc-b6c5-6b8e17295a53)
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/0ffc7a40-73de-4b5c-bf14-3a7ceb6fd36b)
        - 매 줄 주석이 달려 있어서 어떤 작업을 수행했는지 잘 이해가 됐습니다.
    - [x] Step 2. 얼굴 검출 & 랜드마크 검출 하기
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/d28ad6bc-3366-4913-9e93-9145ddcbd22e)
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/d5f692c8-3b82-4a35-9df8-7272e9366998)
        - 매 줄 주석이 달려 있어서 어떤 작업을 수행했는지 잘 이해가 됐습니다.
    - [ ] Step 3. 스티커 적용 위치 확인하기
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/72a4c4fd-fbd8-4e6c-9797-0a0e075ca3ba)
        - 적용 위치를 선정하셨는데, 
    - [ ] step4.스티커 적용하기
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/99af2a5b-0082-44cb-a075-d6153a13e7a4)
    - [ ] Step 5. 문제점 찾아보기
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/399d4ed1-cd1c-4932-b63e-cac8dba82536)
        - 이 부분은 실험이 진행되지 않아서 아쉬웠습니다.

### [ ]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    이 부분은 프로젝트 노트 (LMS) 에 있던 질문 내용을 수행했는지 물어보는 질문으로 변경했습니다. (기존 템플릿 - 성능 평가, 튜닝 실험에 대한 내용은 어울리지 않는것 같아서)
    - [ ] 오늘 배운 np.where 를 사용해서 스티커를 적용해 주세요.
    - [ ] 스티커를 조금 더 자연스럽게 보이게 하려면 어떻게 해야 할까요? 스티커 뒤로 원본 이미지가 같이 보이도록 만들어 봅시다. opencv 의 cv2.addWeighted() 를 참고하세요.
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/edee41c2-3be7-4235-a131-a5d352bc2136)
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/9d8ed4de-84e2-4a47-9aa3-44018323e49a)
img1 과 img2 를 잘못 선정하신것 같아요. 스티커 이미지와 원본이미지를 섞으라는 문제로 이해됐습니다.
    ```
    - [ ]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
    - [ ]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
    - [ ]  각 실험을 시각화하여 비교하였나요?
    - [ ]  모든 실험 결과가 기록되었나요?
    ```

### [x]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - ej 
    - [ ]  배운 점
    - [x]  아쉬운 점
      - cv2.addWeighted() 를 이해 못해 아쉬워 하셨다. 발표 중에 문제에 대해서 이해가 어렵다고 하셨는데, addWeighted 의 documentation 을 보시면 이해에 도움이 되셨을것 같다.
    - [ ]  느낀 점
    - [x]  어려웠던 점
      - 스티커의 위치 ( y 값 계산) 하는 부분이 어려웠다고 하셨다. 이 부분이 왜 어려웠는지 발표에는 말씀해 주셨다. y 값을 변경해 가면서 실험해 보면 이해에 도움이 많이 됐을것 같다.

## 리뷰
