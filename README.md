# ar5iv_zh
 将arxiv上的论文转换成 html 并加入中英对照

 ## 结果
 - （原论文：https://arxiv.org/abs/2305.07185 ）
 - 按段落给出中英对照
 
 <img width="423" alt="image" src="https://github.com/2793145003/ar5iv_zh/assets/24595900/486a6f2c-74bf-4ed4-8fe4-6f85502f4e69">
 
 - 图片 √
 
 <img width="427" alt="image" src="https://github.com/2793145003/ar5iv_zh/assets/24595900/f0b403aa-8f9e-4e94-9b0e-f175cf6dec83">
 
 - 公式 √
 
 <img width="429" alt="image" src="https://github.com/2793145003/ar5iv_zh/assets/24595900/91dc7983-0b50-4d48-9b54-38e9da43f0ef">
 
 - 注释与表格 √

<img width="654" alt="image" src="https://github.com/2793145003/ar5iv_zh/assets/24595900/f09ed19b-f4dd-4c94-a6b4-33db31bd30e7">

## ~~因为自己用得不爽而做出的~~更新
- 2023.5.19
    - 调整了翻译时的格式，现在html标签不会乱了。~~（大概）~~
    - 不过由于要翻译的段落变多了，也更容易443，能不能顺利翻译完要看运气
    - 所以加入了失败重试，希望能管用

 ## 用法
 - 打开 `run.ipynb`
 - 修改论文 ID
 - 运行全部单元格，缺哪个包装哪个包。~~我也不记得我都装了些啥~~
 - 结果在 `./html/paper.html`

## 说明
- 自用，有需要的欢迎自取。
- 咱啥也不会，只会复制粘贴。~~CV 工程师 = ctrl-c + ctrl-v 工程师~~
- 主要代码来自 ChatGPT。
- bug 很多，是否修复看心情。
- 翻译需要挂梯子，可以自己把翻译的API换掉。
- 目前调用翻译 API 过于频繁会报错，长论文记得加 sleep。
