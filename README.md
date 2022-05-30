## 简介

web:vue3+TS+electron+vite<br> 参考项目：https://github.com/caoxiemeihao/electron-vue-vite<br> 备选参考：https://github.com/umbrella22/electron-vite-template<br> api:python+FastAPI

## 项目依赖安装

先安装好 python3.6 以上、node 16 以上

```
  git clone https://gitee.com/i_melon/dnfcalculating_110
  cd api
  pip install fastapi requests uvicorn[standard]

  cd ..
  npm install -g pnpm

  如果依赖安装过慢，可设置镜像
  npm config set registry https://registry.npmmirror.com/
  或
  pnpm add -g nrm
  nrm use taobao

  pnpm install

```

## 项目运行

```
  pnpm dev
```

## 项目进展

### Done

#### api

- [x] 基础类定义实现
- [x] 基础交互 api

#### web

- [x] 基础组件
- [x] 整体页面设计实现

### Doing

#### api

- [ ] 所有词条实现

#### web

- [ ] 称号
- [ ] 宠物
- [ ] 时装
- [ ] 药剂
