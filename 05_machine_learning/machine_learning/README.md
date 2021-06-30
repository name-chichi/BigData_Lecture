# Machine Learning



## Scikit-Learn

- 머신러닝 알고리즘을 구현한 오픈소스 라이브러리

- `SK-Learn` 문법의 공통점

  1. 모델 불러오기 및 정의

     - `hyper-parameter` 세팅

     - ```python
       from sklearn.svm imoprt SVC
       clf = SVC(C=1.0, kernel='rbf', random_state=2019)
       ```

  2. `fit`

     - (훈련)데이터로 모델 학습 또는 특징 추출

     - ```python
       clf.fit(x_train, y_train)
       ```

  3. `predict` or `predict_proba` or `transform`

     - (테스트)데이터 라벨(확률) 예측 또는 변환

     - ```python
       y_pred = clf.predict(x_test)
       ```

  4. `scoring`

     - 정확도, `AUC`, `R2` 등 적절한 스코어 함수로 결과 확인

     - ```python
       accuracy_score(y_test, y_pred)
       ```

  

---



## 1. Linear Regression

- 선형 회귀
- [실습1](./ML01_Linear_Regression_01.ipynb)
- [실습2](./ML02_Linear_Regression_02.ipynb)





## 2. Multiple Linear Regression

- 다중 선형 회귀
- [실습](./ML03_Multiple_Linear_Regression.ipynb)
- [workshop](./ML05_MultipleRegressionWorkshop.ipynb)
- 추가적인 파이썬 모듈 : [pickle](./ML04_pickle.ipynb)





## 3. Classfication

- [분류](./ML06_Classfication.ipynb)