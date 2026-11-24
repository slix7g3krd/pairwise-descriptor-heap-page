# pairwise-descriptor-heap-page

## 领域

游戏、图形与多媒体

## 主题

描述符堆分页与绑定偏移

## 说明

飞行帧回收、设备对齐与脏检查。

初始状态下 `graphics/descriptor_heap_page.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
