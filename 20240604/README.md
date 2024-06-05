##🔑 **PRT(Peer Review Template)**

### [ ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
- 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
- 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개,
  1. 자기만의 카메라앱 기능 구현을 완수하였다.
      - [x] 얼굴 영역과 랜드마크를 정확하게 검출하고, 스티커 사진을 합성시키는 데 성공하였다. ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/9f603d3f-45d0-406d-abbe-acc7914fa4d3)
  2. 스티커 이미지를 정확한 원본 위치에 반영하였다.
      - [ ] 정확한 좌표계산을 통해 고양이 수염의 위치가 원본 얼굴에 잘 어울리게 출력되었다.
        - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/2282cc27-adff-4b33-ae10-0054834fc976) ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/1fc35715-f74a-4b73-9fe9-5a2495d1d796)
  3. 카메라 스티커앱을 다양한 원본이미지에 적용했을 때의 문제점을 체계적으로 분석하였다.
      - [ ] 얼굴각도, 이미지 밝기, 촬영거리 등 다양한 변수에 따른 영향도를 보고서에 체계적으로 분석하였다.
          - 문제점에 대해서 생각을 해봤지만, 문제에 대한 실험을 수행, 결과를 분석하는 부분이 빠져 아쉬웠습니다. ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/399d4ed1-cd1c-4932-b63e-cac8dba82536)

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
    - 적용 위치를 선정하셨는데, 이렇게 설정하신 이유를 잘 모르겠습니다. 이유를 적어주시면 리뷰어가 코드의 이해를 더 잘 할 수 있을것 같아요.
- [ ] step4.스티커 적용하기
    - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/99af2a5b-0082-44cb-a075-d6153a13e7a4)
    - 각 부분이 어떤 기능을 하는지 적혀있다면 좋을것 같습니다.
- [ ] Step 5. 문제점 찾아보기
    - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/399d4ed1-cd1c-4932-b63e-cac8dba82536)
    - 이 부분은 실험이 진행되지 않아서 아쉬웠습니다.

### [ ]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
이 부분은 프로젝트 노트 (LMS) 에 있던 질문 내용을 수행했는지 물어보는 질문으로 변경했습니다. (기존 템플릿 - 성능 평가, 튜닝 실험에 대한 내용은 어울리지 않는것 같아서)
- [x] 고양이 수염이 적용 될 위치를 landmark를 사용해서 계산해 주세요. 제대로 된 위치가 선정 됐고, 이미지에 제대로 된 위치가 표시됐는지?
    - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/2282cc27-adff-4b33-ae10-0054834fc976)
    - 33 번보다 좋은 위치로 30 번을 선정하셨습니다.
    - 그런데 y 값을 30 번 위치 + 얼굴영역의 높이의 절반 으로 하신 이유가 적혀져 있지 않습니다.
    - 아래의 코드를 보고 이해했습니다. 두 부분을 합쳐 생각하면 결국, 30 번 위치를 중앙에 놓는 사각형의 top-left 좌표를 가르키도록 하셨군요.
    - **스티커가 적용 될 위치를 landmark를 사용해서 계산해 주셨습니다.**
    - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/1fc35715-f74a-4b73-9fe9-5a2495d1d796)
    - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/9f603d3f-45d0-406d-abbe-acc7914fa4d3)
    - **제대로 된 위치가 선정 됐고, 이미지에 제대로 된 위치가 표시됐습니다.**
- [ ] 오늘 배운 np.where 를 사용해서 스티커를 적용해 주세요.
    - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/aa907586-bbcd-4d13-8e5d-fe4b2b026ff5)
    - img1 값이 img2 값보다 클 때, img1 이 선택되도록 코드를 짜셨네요. 그리고 img1 과 img2 가 각각 sticker 추가된 이미지의 rgb 와 bgr 버전이어서 green channel은 반영이 안되고, 보라색과 (b > r), 주홍색(r > b)에 대한 색만 반영이 될 것 같아요. 문제에서 의도한 바와는 다른 구현인것 같습니다.
- [ ] 스티커를 조금 더 자연스럽게 보이게 하려면 어떻게 해야 할까요? 스티커 뒤로 원본 이미지가 같이 보이도록 만들어 봅시다. opencv 의 cv2.addWeighted() 를 참고하세요.
    - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/edee41c2-3be7-4235-a131-a5d352bc2136)
    - ![image](https://github.com/hojae-m-choi/first-repository/assets/98305832/9d8ed4de-84e2-4a47-9aa3-44018323e49a)
img1 과 img2 를 잘못 선정하신것 같아요. 스티커 이미지와 원본이미지를 섞으라는 문제로 이해됐습니다.

- 이전 항목들
```
- [ ]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
- [ ]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
- [ ]  각 실험을 시각화하여 비교하였나요?
- [ ]  모든 실험 결과가 기록되었나요?
```

### [ ]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
회고가 상세히 기록되어 있지 않아서 아쉬웠습니다.
- [ ]  배운 점
- [x]  아쉬운 점
  - cv2.addWeighted() 를 이해 못해 아쉬워 하셨다. 발표 중에 문제에 대해서 이해가 어렵다고 하셨는데, addWeighted 의 documentation 을 보시면 이해에 도움이 되셨을것 같다.
- [ ]  느낀 점
- [x]  어려웠던 점
  - 스티커의 위치 ( y 값 계산) 하는 부분이 어려웠다고 하셨다. 이 부분이 왜 어려웠는지 발표에는 말씀해 주셨다. y 값을 변경해 가면서 실험해 보면 이해에 도움이 많이 됐을것 같다.

## 리뷰
고생 많으셨습니다. 다양한 이미 상황에 대해서 실험을 수행하지 않은 부분이 아쉬웠습니다.

