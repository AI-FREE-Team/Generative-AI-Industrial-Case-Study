# 單元四、生成式 AI 工具輸出驗證方法

## 1. 前言
在這一單元，我們主要討論該如何**驗證生成式AI輸入的程式碼可用性**，有的時候因為生成式AI工具並沒有獲得完整的背景知識或是需求，因此生成的程式碼雖然可以使用（如果不能執行那反而比較好，因為工程師這時候一定會介入修復），但是會存在一些漏洞，或是執行的效能不如預期；而這樣的情況其實就跟我們一般的軟體工程師偶爾會犯錯一樣，當然AI也有可能在部分情況失誤，因此這時候是否存在一個測試框架就很重要了。

## 2. 軟體開發常見檢驗方法
常見的測試框架大致包含：單元測試（Unit Testing）、集成測試（Integration Testing）、系統測試（System Testing）、壓力測試（Stress Testing）

### 2.1 單元測試（Unit Testing）
這是最基本的測試，主要針對軟體系統當中的單個模組進行測試。目的是確保每個部分都可以正常工作。

### 2.2 集成測試（Integration Testing）
當所有單一模組都通過了單元測試確認運作正常之後，就可以進入此步驟，利用集成測試將這些模組整合起來測試，以確保它們在彼此串聯的情況下也能正常運作。

### 2.3 系統測試（System Testing）
在這邊則是關注於整體系統是否有如預期的運作，預期就與規格相關，對於每個軟體系統的產品管理師（Product Manager）一定都會有一張該系統需要滿足的剛性指標與軟性指標，剛性指標可能包含，這個軟體系統的失誤率要在0.005%以下；而軟性指標則可能是，此軟體系統在正常運作的過程中，要在2.5秒內給予使用者回饋。

### 2.4 壓力測試（Stress Testing）
在具備規模的軟體公司服務中，其用戶數量可能達上萬人，這樣的情況下，任何的新功能要上架前基本上都會需要經過壓力測試，要去測試這個功能是否能夠承擔短時間高流量的Request，因此軟體開發部門就會在測試的階段，故意營造類似[DDoS](https://www.cloudflare.com/zh-tw/learning/ddos/what-is-a-ddos-attack/)的大量Request事件，確認伺服器與系統都能夠正常運轉。

## 3. 實際測試（以單元測試為例）

我們在上一的單元實際展示了如何利用生成式AI工具協助我們開發一個智能語音助理的系統，屬於自然語言處理服務的範疇。在這個單元，我們則改為利用電腦視覺的服務，向讀者展示實際上可以如何透過軟體自動化的方式，自行檢測任何的程式碼，即使是生成式AI所生成的程式碼也能夠透過此方案進行驗證。

### 3.1 單元測試介紹
單元測試是軟體開發的一項基礎工作，對程式碼的最小可測試部分進行驗證，確保它們按預期工作。通過單元測試，開發者可以在早期階段發現錯誤，減少調整時間，並提高程式碼質量。

### 3.2 生成式AI的角色
在單元測試的撰寫中，生成式AI工具，像是ChatGPT，我們使用者可以透過ChatGPT直接的生成測試代碼。這種AI技術可以理解複雜的程式撰寫概念，提供單元測試的起點/模板，進而加快開發週期。而這步驟若是讀者不放心，也可以自行撰寫單元測試的測試程式碼，只是向讀者說明，如果時間上比較急迫，或許可以考慮使用GPT協助生成測試程式碼。

### 3.3 電腦視覺服務
為了演示如何使用ChatGPT進行單元測試，我們將撰寫一段專門用於圖像處理的Python程式碼。

這段程式碼包括數個函數（Function）：
1. 轉換圖像為灰階
2. 提高畫面解析度
3. 使用高斯模糊
4. 提高影像對比度
5. 將圖像保存為JPG格式

我們使用Lena作為驗證用的影像，並將程式碼寫入`image_processing.py`當中。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit4/lena.png" width="600px">
</div>

```python
import cv2
import numpy as np

img = cv2.imread('lena.png')

# 1. 將圖像轉換為灰階
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. 通過應用銳化來提升圖像質量
def enhance_image_quality(image):
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

# 3. 對圖像應用高斯模糊
def apply_gaussian_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)

# 4. 對圖像進行直方圖均衡化
def histogram_equalization(image):
    if len(image.shape) == 2:  # 灰階圖像
        return cv2.equalizeHist(image)
    else:  # 彩色圖像
        ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

# 5. 將文件轉換為JPG
def convert_to_jpg(image, filename):
    cv2.imwrite(f'{filename}.jpg', image)


gray_image = convert_to_grayscale(img)
enhanced_image = enhance_image_quality(img)
blurred_image = apply_gaussian_blur(img)
equalized_image = histogram_equalization(gray_image)  
convert_to_jpg(img, 'lena_converted')
```

### 3.4 撰寫單元測試程式碼
在此我們清楚地向ChatGPT說明我們的需求，並請他協助為每個函數生成對應的測試程式碼：

#### 測試轉換為灰階功能：`test_convert_grayscale`
這個測試檢查 `convert_to_grayscale` 函數是否正確地將一個彩色圖像轉換成灰階圖像。灰階圖像應該只有二維（高度和寬度），而不是三維（還包括顏色通道）。測試通過比較轉換後圖像的維度來確認這一點。

#### 測試提升圖像質量功能：`test_enhance_image_quality`
這個測試檢查 `enhance_image_quality` 函數是否在不改變圖像尺寸的情況下提升了圖像的質量。測試通過確保增強後的圖像與原始圖像有相同的形狀來確認這一點。

#### 測試應用高斯模糊功能：`test_apply_gaussian_blur`
這個測試檢查 `apply_gaussian_blur` 函數是否正確地對圖像應用了高斯模糊效果。測試確保模糊後的圖像與原始圖像有相同的尺寸。

#### 測試直方圖均衡化功能：`test_histogram_equalization`
這個測試檢查 `histogram_equalization` 函數是否正確地對灰階圖像進行了直方圖均衡化。均衡化是圖像處理中用於改善圖像對比度的常用方法。測試通過確保均衡化後的圖像與原始灰階圖像有相同的尺寸來驗證功能的正確性。

#### 測試將文件轉換為JPG格式功能：`test_convert_to_jpg`
這個測試檢查 `convert_to_jpg` 函數是否能夠將圖像保存為 JPG 格式的文件。測試通過檢查文件系統中是否存在轉換後的文件來確認函數的正確性。這個測試假定函數會在當前工作目錄中創建一個新的 JPG 文件。

以下是實際的測試程式碼：`test_image.py`

```python
import unittest
from image_processing import convert_to_grayscale,enhance_image_quality,apply_gaussian_blur,histogram_equalization,convert_to_jpg
import os
import cv2

# 單元測試類
class TestImageProcessingFunctions(unittest.TestCase):

    def setUp(self):
        # 讀取Lena圖像檔案
        self.test_image = cv2.imread('lena.png')
        if self.test_image is None:
            raise FileNotFoundError("無法找到lena.png圖像檔案。")
        self.test_gray_image = cv2.cvtColor(self.test_image, cv2.COLOR_BGR2GRAY)

    def test_convert_to_grayscale(self):
        # 測試轉換為灰階的功能
        gray_image = convert_to_grayscale(self.test_image)
        self.assertEqual(len(gray_image.shape), 2, "圖像應該被轉換為灰階。")

    def test_enhance_image_quality(self):
        # 測試提升圖像質量的功能
        enhanced_image = enhance_image_quality(self.test_image)
        self.assertEqual(enhanced_image.shape, self.test_image.shape, "增強後的圖像應該與原始圖像大小相同。")

    def test_apply_gaussian_blur(self):
        # 測試應用高斯模糊的功能
        blurred_image = apply_gaussian_blur(self.test_image)
        self.assertEqual(blurred_image.shape, self.test_image.shape, "模糊後的圖像應該與原始圖像大小相同。")

    def test_histogram_equalization(self):
        # 測試直方圖均衡化功能
        equalized_image = histogram_equalization(self.test_gray_image)
        self.assertEqual(equalized_image.shape, self.test_gray_image.shape, "均衡化後的圖像應該與原始灰階圖像大小相同。")

    def test_convert_to_jpg(self):
        # 測試將文件轉換為JPG格式的功能
        filename = 'lena_converted'
        convert_to_jpg(self.test_image, filename)
        self.assertTrue(os.path.exists(f'{filename}.jpg'), "轉換後的JPG文件應該存在。")

# 當執行此文件為主程序時運行測試
if __name__ == '__main__':
    unittest.main()
```

### 3.5 測試結果
運行ChatGPT生成的測試代碼後，我們得到了以下結果：所有五個測試都在短短0.041秒內完成，且全部通過，這證明了我們的圖像處理函數按預期進行。
<div align=center>
<img src="https://github.com/AI-FREE-Team/Generative-AI-Industrial-Case-Study/blob/main/%E6%95%99%E6%A1%884%EF%BC%9A%E7%A8%8B%E5%BC%8F%E7%94%9F%E6%88%90%E8%88%87%E8%BC%94%E5%8A%A9/pics/unit4/test.png" width="600px">
</div>

## 4. 結論
生成式AI，特別是ChatGPT，展現了在單元測試方面的強大潛力。它不僅可以提升開發效率，還能幫助開發者專注於更複雜的任務。雖然AI生成的測試需要經過人工審核以確保其完整性和正確性，但透過這個流程，我們就能夠進一步驗證生成式AI所撰寫的程式碼了！