# Getting A Simple Program running from Scratch

When I try to run the code `python src/test.py` with just 2 lines of code I saw the following error.

```
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems % python src/test.py
Traceback (most recent call last):
  File "/Users/sma54/SAN/GIT_HUB/DESIGN_MULTI_AGENT_SYSTEM/book-designing-multiagent-systems/.venv/lib/python3.12/site-packages/picoagents/llm/_anthropic.py", line 15, in <module>
    from anthropic import (
ModuleNotFoundError: No module named 'anthropic'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/sma54/SAN/GIT_HUB/DESIGN_MULTI_AGENT_SYSTEM/book-designing-multiagent-systems/src/test.py", line 2, in <module>
    from picoagents import Agent
  File "/Users/sma54/SAN/GIT_HUB/DESIGN_MULTI_AGENT_SYSTEM/book-designing-multiagent-systems/.venv/lib/python3.12/site-packages/picoagents/__init__.py", line 47, in <module>
    from .agents import (
  File "/Users/sma54/SAN/GIT_HUB/DESIGN_MULTI_AGENT_SYSTEM/book-designing-multiagent-systems/.venv/lib/python3.12/site-packages/picoagents/agents/__init__.py", line 8, in <module>
    from ._agent import Agent
  File "/Users/sma54/SAN/GIT_HUB/DESIGN_MULTI_AGENT_SYSTEM/book-designing-multiagent-systems/.venv/lib/python3.12/site-packages/picoagents/agents/_agent.py", line 40, in <module>
    from ._base import AgentToolError, BaseAgent
  File "/Users/sma54/SAN/GIT_HUB/DESIGN_MULTI_AGENT_SYSTEM/book-designing-multiagent-systems/.venv/lib/python3.12/site-packages/picoagents/agents/_base.py", line 19, in <module>
    from ..llm import BaseChatCompletionClient
  File "/Users/sma54/SAN/GIT_HUB/DESIGN_MULTI_AGENT_SYSTEM/book-designing-multiagent-systems/.venv/lib/python3.12/site-packages/picoagents/llm/__init__.py", line 8, in <module>
    from ._anthropic import AnthropicChatCompletionClient
  File "/Users/sma54/SAN/GIT_HUB/DESIGN_MULTI_AGENT_SYSTEM/book-designing-multiagent-systems/.venv/lib/python3.12/site-packages/picoagents/llm/_anthropic.py", line 25, in <module>
    raise ImportError(
ImportError: Anthropic library not installed. Please install with: pip install anthropic>=0.73.0
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems %
```
I installed the following library.

`uv pip install "anthropic>=0.73.0"`

```
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems % uv pip install "anthropic>=0.73.0"
Resolved 16 packages in 689ms
Prepared 1 package in 553ms
Installed 2 packages in 7ms
 + anthropic==0.75.0
 + docstring-parser==0.17.0
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems %
```

Error is now gone.

```
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems % python src/test.py
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems %
```

I then installed `python-dotenv`

```
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems % uv pip install python-dotenv
Resolved 1 package in 4.72s
Prepared 1 package in 399ms
Installed 1 package in 9ms
 + python-dotenv==1.2.1
 ```

After adding the test code, the output is below.

```
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems % python src/test.py
Poet says: [poet] 08:19:43 | duration: 1.5s, tokens: in:26, out:23 | finish: stop
(book-designing-multiagent-systems) sma54@UKYXG4XTV7RY book-designing-multiagent-systems %
```

I do not see the Poet response in the output
