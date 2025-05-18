# Stable Diffusion 기반 이미지 생성에 따른 학습 데이터 효율화 연구

#### Stable Diffusion을 활용하여 인공 데이터셋을 생성하고 이를 실제 데이터셋과의 비율을 조절하며 실제 학습에 효율적인지 연구


## 연구 개요

* 생성형 AI를 사용하면 데이터 부족 문제를 해결하거나 데이터의 일반화 성능 향상 가능성을 제공할 수 있는가?
* ResNet18과 Stable Diffusion을 이용하여 인공 이미지와 실제 이미지의 비율을 조정하여 성능 비교


## 사용한 모델과 언어
#### 사용한 모델
* Stable Diffusion
* ResNEt

#### 사용한 언어 및 라이브러리
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)


## 생성한 가상 이미지 및 사용한 프롬프트
<p align="center">
  <img src="https://github.com/user-attachments/assets/373d65fd-47b3-4597-83b4-0b67230fa173" width="45%"/>
  <img src="https://github.com/user-attachments/assets/4403018d-fe5f-4589-90be-a957cabc9e33" width="45%"/>
</p>

```
“A photorealistic, highly detailed 8K photograph of a turtle in various settings and poses in the sea, shot with a Nikon Z7 II, 70-200mm lens, natural lighting, sharp focus, ultra-high-definition”
```
#### 위 Prompt를 통해 가상이미지를 생성하고 생성한 데이터와 실제 데이터를 합친 Dataset 구성


### 데이터셋 
* Total Class : 6개 (Bear, Dog, Cat, turtle, Dear, Eagle)
  * 구성: 
    * Train : 1348
    * Val : 162
    * Test : 162
      
  * 이때 Test Data는 오직 실제 이미지 데이터만 사용하여 Test
  * Fake:Real = 5:5, 6:4, 7:3, 8:2

![image](https://github.com/user-attachments/assets/2d281b6f-dea9-4bb3-ad18-8d0c82bcfafd)


## 연구 방법
1. Stable Diffusion을 이용하여 각 클래스에 맞는 이미지 생성
2. Fake의 비율을 조절하여 데이터셋을 나누어 ResNet18을 이용하여 전이학습(Image Classification)
3. 동일한 Test Dataset을 통해 Test Accuracy를 확인하고 비교


## 연구 결과
| Dataset               | Test Accuracy |   
|-----------------------|---------------|
| 실제 이미지 100%      | 98.15%        |
| 5:5로 나눈 데이터셋   | 95.06%        |
| 6:4로 나눈 데이터셋   | 97.55%        |
| 7:3로 나눈 데이터셋   | 94.87%        |
| 8:2로 나눈 데이터셋   | 94.20%        |

![image](https://github.com/user-attachments/assets/5b8c0b20-2f67-4410-b0a6-fc16450c94c4)

#### 각 데이터셋의 Test Accuracy를 비교한 결과
* 가장 높은 Accuracy는 실제 이미지로만 구성된 데이터셋
* 두번쨰로 높은 것은 6:4로 구성된 데이터 - 인공 데이터를 효과적으로 이용
* 5:5, 7:3, 8:2 에서는 실제 이미지로만 구성된 데이터셋보다 낮은 성능을 보임

:mag_right: 인공 이미지 비율이 과도하게 많아질 경우, 모델의 일반화 성능 감소 존재
### 따라서 인공이미지와 실제 이미지의 균형이 중요


## 결론
생성형 AI를 이용하여 이미지를 생성하여 데이터셋으로 활용할 수 있는 가능성 확인
데이터가 부족한 상황이 발생할 시 AI로 생성한 이미지를 활용한다면 데이터의 부족 문제 해결 가능성 존재


### 프롬프트 최적화 기법을 효과적으로 활용하면, 원하는 데이터를 목적에 맞게 정밀하게 생성 가능
### 특히 이미지 데이터를 수집하기 어려운 분야에서는, 이를 통해 대체 학습 데이터를 확보하거나 데이터 다양성을 높이는 데 큰 도움이 될 것으로 기대



#### 참조 논문
1. JHe,K.Zhang, X., Ren, S., & Sun, J. (2016). Deep Residual Learning for Image Recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 770–778. https://doi.org/10.1109/CVPR.2016.90
2. F. A. Croitoru, V. Hondru, R. T. Ionescu and M. Shah, "Diffusion Models in Vision: A Survey," in IEEE Transactions on Pattern Analysis and Machine Intelligence, doi:10.1109/TPAMI.2023.3268241

#### 본 연구는 2024년 과학기술정보통신부 및 정보통신기획평가원의 SW중심대학사업의 지원을 받아 수행되었습니다. (2024-0-00047)










