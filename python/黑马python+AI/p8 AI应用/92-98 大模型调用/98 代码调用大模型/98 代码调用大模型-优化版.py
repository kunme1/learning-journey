"""来源：98 代码调用大模型.py；配套：98 代码调用大模型-优化版.md。
整理日期：2026-11-27（北京时间）。原始文件保留；改写理由见就近注释。
"""

import os
from openai import OpenAI


def extract_answer(response):
    """原直接choices[0].message.content；显式检查空候选和空正文，定位响应问题。"""
    if not response.choices:
        raise ValueError("响应中没有候选回答。")
    content = response.choices[0].message.content
    if not isinstance(content, str) or not content.strip():
        raise ValueError("响应没有非空文本正文，请检查完成原因。")
    return content  # 保留实际回答内容，不strip掉有意义的排版。


def request_answer(client):
    # 原参数和人设／问题保留，抽函数方便本地MockTransport验证而不调用公网。
    # deepseek-flash与两个思考控制项已核对本次DeepSeek官方契约，不按旧教材降回旧名称。
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": "你是一名非常可爱的AI助理，你的名字叫小言言，请你使用温柔可爱的语气回答用户的问题。"},
            {"role": "user", "content": "我现在有12个苹果，3个人，怎么均分？"},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )
    return extract_answer(response)


def main():
    # 原直接get后创建客户端，空变量在SDK里才失败；现在先给出明确配置提示，不输出密钥。
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key or not api_key.strip():
        raise ValueError("当前进程未读取到DEEPSEEK_API_KEY，请检查启动环境。")
    # 前瞻：with确保客户端连接关闭；timeout明确等待上限，max_retries=0关闭自动重试。
    # 与SDK默认策略不同：超时或服务错误交给调用者处理，本文件不自动重复付费请求。
    with OpenAI(api_key=api_key, base_url="https://api.deepseek.com", timeout=30.0, max_retries=0) as client:
        print(request_answer(client))


# 原脚本导入即发请求；入口保护让import只定义功能，直接运行仍会进行一次真实调用。
# 安装包应使用运行脚本的同一解释器：<解释器路径> -m pip install openai。
if __name__ == "__main__":
    main()
