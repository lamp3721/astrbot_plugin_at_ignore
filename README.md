# astrbot_plugin_at_ignore

让 AstrBot 忽略所有 @ 它的消息，不进行任何响应和 LLM 处理。

## 功能

- 当有人 @ 机器人时，机器人将**完全忽略**该消息
- 使用最高优先级拦截，确保在其他处理器之前执行
- 调用 `event.stop_event()` 阻止后续的 LLM 处理

## 安装

### 方式一：插件市场安装（推荐）

在 AstrBot 管理面板的插件市场中搜索 `astrbot_plugin_at_ignore` 并安装。

### 方式二：手动安装

```bash
cd data/plugins
git clone https://github.com/lamp3721/astrbot_plugin_at_ignore.git
```

重启 AstrBot 即可生效。

## 使用

安装后无需配置，插件会自动拦截所有 @ 机器人的消息。

## 日志

插件会在 debug 级别记录被拦截的消息：

```
[忽略@] 拦截来自 用户名(用户ID) 的 @ 消息
```

## 许可证

GPL-3.0
