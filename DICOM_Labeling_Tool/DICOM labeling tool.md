# DICOM Labeling Tool

Dicom을 레이블링 할 수 있는 pyqt 기반의 코드입니다.

# 필요 패키지

1. PyQt
2. pandas
3. cv2
4. SimpleITK
5. numpy

# 준비물

## labeling.csv

다음과 같은 column들로 구성되어 있어야 합니다.

```python
,filePath,RelabeledColumn
```

이 때 `RelabeledColumn`은 dummy 값 아무거나로 채워도 됩니다. `None`도 가능합니다.

가능하다면, `filePath`는 파일의 절대경로를 입력하세요.

## DICOM_labeling_tool.py

(17번째 줄)[https://github.com/jryoungw/DICOM_Tools/blob/master/DICOM_Labeling_Tool/DICOM_labeling.py#L17]인

```python
self.labels = [first, second, ...]
```

에 본인이 원하는 target 값들을 지정해 놓으세요. 기본 값은 `good`과 `bad`입니다. 꼭 두 개일 필요가 없지만 `9개 이하의 label들만 지원합니다`. 더 많은 label을 필요로 하는 상황이라면 `29번째 줄`인 `exec`구문을 직접 노가다로 설정해 주어야 합니다.

# 실행법

1. 커맨드 창에서 `python DICOM_labeling.py`를 수행합니다.
2. `Open CSV` 버튼을 클릭합니다. 이 버튼으로 csv파일을 열게 되면, `filePath` 칼럼에 있던 경로의 이미지들을 읽게 됩니다.
3. `View Image` 버튼을 클릭합니다. 경우에 따라서 이미지 사이즈가 큰 경우에는 최대화를 해도 이미지가 잘리는 경우가 있을 수 있습니다.
4. `1`번부터 `9`번까지의 키보드 버튼을 클릭하면 17번째 줄에서 설정해놓은 항목들로 이미지가 label되게 됩니다. 매 키보드를 누를 때마다 자동저장이 됩니다.
5. 만약 잘못 레이블링한 경우, `Backward` 버튼을 눌러 전 이미지들로 돌아가서 재레이블 할 수 있습니다.
6. `Save Result`는 중간 결과 저장입니다. `filePath` 칼럼의 모든 이미지가 레이블링 되었다면 `DICOM_labeling.py`는 자동으로 꺼지게 됩니다. 저장 파일은 `labeling_relabeled.csv` 파일명으로 저장되게 됩니다.
