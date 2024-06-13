🔑 **PRT(Peer Review Template)**
> written by 제민욱

- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부

<img width="481" alt="Screenshot 2024-06-13 at 5 36 40 PM" src="https://github.com/minkj1992/first-repository/assets/37536298/009ee225-a5af-4e2b-98b2-edc835b855d2">


문제에서 요구하는 모든 조건들을 만족했습니다. 다만 `summa.summarizer.summarize`가 내부적인 버그가 존재하는 것 같습니다.
예를들면 일정 횟수 이상 사용하면 None을 return하는 케이스가 존재한 것으로 보입니다.

- [x]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
    - [x]  모델 선정 이유
    - [x]  Metrics 선정 이유
    - [x]  Loss 선정 이유

<img width="858" alt="Screenshot 2024-06-13 at 5 37 33 PM" src="https://github.com/minkj1992/first-repository/assets/37536298/463002a6-936f-47c9-a4f4-0b0778b3e767">

seq2seq에 attention 매커니즘을 적용하여 성공적으로 처리를 하였습니다.

- [x]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    - [x]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
    - [x]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
    - [x]  각 실험을 시각화하여 비교하였나요?
    - [x]  모든 실험 결과가 기록되었나요?

- [x]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - [x]  배운 점
    - [x]  아쉬운 점
    - [x]  느낀 점
    - [x]  어려웠던 점

<img width="730" alt="Screenshot 2024-06-13 at 5 37 09 PM" src="https://github.com/minkj1992/first-repository/assets/37536298/1b5ebf06-2814-49b7-92fa-ed6c388440b9">


다른 분들도 `summa.summarizer.summarize`가 None을 return하는 이슈가 있었는데, 은경님도 똑같은 이슈를 경험하신 것 같습니다.
