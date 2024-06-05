🔑 **PRT(Peer Review Template)**
 Reviewer : 맹주현
 
- [ ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부
     
    - [ ]  1. 인물모드 사진을 성공적으로 제작하였다.
    - [X]  2. 제작한 인물모드 사진들에서 나타나는 문제점을 정확히 지적하였다.
    - [ ]  3. 인물모드 사진의 문제점을 개선할 수 있는 솔루션을 적절히 제시하였다.
     
![1](https://github.com/ek0111/first-repository/assets/168398983/6946d873-4fb2-42f7-b3fd-256abb5ae361)

![2](https://github.com/ek0111/first-repository/assets/168398983/d5271f48-9dd7-4fc4-821e-b3a2e1878a41)

![3](https://github.com/ek0111/first-repository/assets/168398983/26d64ade-a722-4e98-95d1-63253047d12b)

![4](https://github.com/ek0111/first-repository/assets/168398983/42696e1b-b82f-45ee-a5c0-95ed68569d58)

일반적인 ML segmentation 관점에서 해결 방법을 모색하신 것 같아요. DL 관점에서 segmentation 성능을 향상 시키기 위한 고민도 해보시면 더 좋을 것 같습니다! 

- [X]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
    - [ ]  모델 선정 이유
    - [ ]  Metrics 선정 이유
    - [ ]  Loss 선정 이유
![7](https://github.com/ek0111/first-repository/assets/168398983/6c0af03d-a370-4694-b5d6-3e4b428c35c2)

![6](https://github.com/ek0111/first-repository/assets/168398983/692a5f0e-0c9d-458c-a27b-06c0e49070f1)

노드와 다르게 본인 코드로 작성한 부분은 주석으로 설명해놓으셨다. 


- [ ]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    - [ ]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
    - [ ]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
    - [ ]  각 실험을 시각화하여 비교하였나요?
    - [ ]  모든 실험 결과가 기록되었나요?

오늘은 Pre-Trained model로 실습하는 날이었기 때문에 3 번은 넘어갔습니다. 

- [X]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - [X]  배운 점
    - [X]  아쉬운 점
    - [X]  느낀 점
    - [X]  어려웠던 점

![5](https://github.com/ek0111/first-repository/assets/168398983/a0cb1971-26eb-423f-aa6e-d076e22e6c34)

## 리뷰

2번에서 객체를 blur로 변경하기 위해, seg_color = (0, 0, 0) 으로 놓고 진행하셨는데, 
img_concat2 = np.where(img_mask_color2==255,   img_orig2 ,img_bg_blur2)
이 부분에서 img_bg_blur2랑 img_orig2의 위치를 바꾸는 식으로도 가능합니다!

