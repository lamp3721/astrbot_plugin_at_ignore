"""
AstrBot 插件 - 忽略 @ 消息
当机器人被 @ 时，忽略该消息，不进行任何响应和 LLM 处理。
"""
from sys import maxsize

import astrbot.api.message_components as Comp
from astrbot.api import logger
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register


@register(
    "astrbot_plugin_at_ignore",
    "lamp",
    "忽略 @ 消息，bot 不会响应任何 @ 它的消息",
    "1.0.0",
    "https://github.com/lamp3721/astrbot_plugin_at_ignore",
)
class IgnoreAtPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        logger.info("忽略 @ 插件已加载")

    @filter.event_message_type(filter.EventMessageType.ALL, priority=maxsize)
    async def ignore_at_messages(self, event: AstrMessageEvent):
        """
        拦截所有 @ 机器人的消息并阻止后续处理。
        使用最高优先级 (maxsize) 确保在其他处理器之前执行。
        """
        messages = event.get_messages()
        bot_id = str(event.get_self_id())

        # 检查消息中是否有 @ 机器人
        for message in messages:
            if isinstance(message, Comp.At):
                # 检查是否 @ 的是机器人自己
                if str(message.qq) == bot_id:
                    logger.debug(
                        f"[忽略@] 拦截来自 {event.get_sender_name()}({event.get_sender_id()}) 的 @ 消息"
                    )
                    # 终止事件传播，阻止后续的 LLM 处理和其他响应
                    event.stop_event()
                    return

    async def terminate(self):
        """插件被卸载/停用时调用"""
        logger.info("忽略 @ 插件已卸载")